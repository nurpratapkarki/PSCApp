import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, TouchableOpacity, Alert, KeyboardAvoidingView, Platform } from 'react-native';
import { Stack, useRouter } from 'expo-router';
import { Card, Text, TextInput, Button, Avatar, ActivityIndicator, Chip } from 'react-native-paper';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useApi } from '../../hooks/useApi';
import { User } from '../../types/auth.types';
import { Branch } from '../../types/category.types';
import { Colors } from '../../constants/colors';
import { Spacing, BorderRadius } from '../../constants/typography';

export default function EditProfileScreen() {
  const router = useRouter();
  const { data: user, status: userStatus } = useApi<User>('/api/auth/user/');
  const { data: branches } = useApi<Branch[]>('/api/branches/');

  const [fullName, setFullName] = useState(user?.profile?.full_name || '');
  const [phone, setPhone] = useState(user?.profile?.phone_number || '');
  const [selectedBranch, setSelectedBranch] = useState<number | null>(user?.profile?.branch || null);
  const [isSaving, setIsSaving] = useState(false);

  React.useEffect(() => {
    if (user) {
      setFullName(user.profile?.full_name || '');
      setPhone(user.profile?.phone_number || '');
      setSelectedBranch(user.profile?.branch || null);
    }
  }, [user]);

  const handleSave = async () => {
    setIsSaving(true);
    setTimeout(() => {
      setIsSaving(false);
      Alert.alert('Success', 'Profile updated successfully!', [{ text: 'OK', onPress: () => router.back() }]);
    }, 1500);
  };

  if (userStatus === 'loading') {
    return (
      <SafeAreaView style={styles.loaderContainer}>
        <ActivityIndicator size="large" color={Colors.primary} />
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <Stack.Screen options={{ headerShown: false }} />
      <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <MaterialCommunityIcons name="arrow-left" size={24} color={Colors.textPrimary} />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Edit Profile</Text>
          <View style={{ width: 44 }} />
        </View>

        <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          {/* Avatar Section */}
          <View style={styles.avatarSection}>
            <View style={styles.avatarContainer}>
              <Avatar.Image size={100} source={{ uri: user?.profile?.profile_picture || `https://i.pravatar.cc/150?u=${user?.email}` }} />
              <TouchableOpacity style={styles.changeAvatarBtn}>
                <MaterialCommunityIcons name="camera" size={20} color={Colors.white} />
              </TouchableOpacity>
            </View>
            <Text style={styles.changePhotoText}>Tap to change photo</Text>
          </View>

          {/* Form */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Full Name</Text>
              <TextInput mode="outlined" placeholder="Enter your full name" value={fullName} onChangeText={setFullName} style={styles.textInput} outlineColor={Colors.border} activeOutlineColor={Colors.primary} left={<TextInput.Icon icon="account" />} />

              <Text style={styles.inputLabel}>Email</Text>
              <TextInput mode="outlined" value={user?.email || ''} style={styles.textInput} outlineColor={Colors.border} disabled left={<TextInput.Icon icon="email" />} />

              <Text style={styles.inputLabel}>Phone Number</Text>
              <TextInput mode="outlined" placeholder="Enter phone number" value={phone} onChangeText={setPhone} keyboardType="phone-pad" style={styles.textInput} outlineColor={Colors.border} activeOutlineColor={Colors.primary} left={<TextInput.Icon icon="phone" />} />
            </Card.Content>
          </Card>

          {/* Branch Selection */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Preferred Branch</Text>
              <View style={styles.branchGrid}>
                {branches?.map((branch) => (
                  <Chip key={branch.id} selected={selectedBranch === branch.id} onPress={() => setSelectedBranch(branch.id)} style={styles.branchChip} selectedColor={Colors.primary}>
                    {branch.name_en}
                  </Chip>
                ))}
              </View>
            </Card.Content>
          </Card>
        </ScrollView>

        {/* Save Button */}
        <View style={styles.bottomAction}>
          <Button mode="contained" icon="content-save" style={styles.saveButton} contentStyle={styles.saveButtonContent} labelStyle={styles.saveButtonLabel} onPress={handleSave} loading={isSaving} disabled={isSaving}>
            Save Changes
          </Button>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  loaderContainer: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: Colors.background },
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', padding: Spacing.base },
  backButton: { width: 44, height: 44, borderRadius: 22, backgroundColor: Colors.white, alignItems: 'center', justifyContent: 'center', elevation: 2 },
  headerTitle: { fontSize: 20, fontWeight: '700', color: Colors.textPrimary },
  scrollContent: { padding: Spacing.base, paddingBottom: 100 },
  avatarSection: { alignItems: 'center', marginBottom: Spacing.xl },
  avatarContainer: { position: 'relative' },
  changeAvatarBtn: { position: 'absolute', bottom: 0, right: 0, width: 36, height: 36, borderRadius: 18, backgroundColor: Colors.primary, alignItems: 'center', justifyContent: 'center', borderWidth: 3, borderColor: Colors.background },
  changePhotoText: { fontSize: 13, color: Colors.primary, marginTop: Spacing.sm },
  card: { backgroundColor: Colors.white, borderRadius: BorderRadius.xl, marginBottom: Spacing.lg, elevation: 2 },
  inputLabel: { fontSize: 14, fontWeight: '600', color: Colors.textPrimary, marginBottom: Spacing.xs, marginTop: Spacing.md },
  textInput: { backgroundColor: Colors.white },
  branchGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: Spacing.xs },
  branchChip: { marginBottom: Spacing.xs },
  bottomAction: { backgroundColor: Colors.white, padding: Spacing.base, borderTopWidth: 1, borderTopColor: Colors.border },
  saveButton: { borderRadius: BorderRadius.lg },
  saveButtonContent: { paddingVertical: Spacing.sm },
  saveButtonLabel: { fontSize: 16, fontWeight: '700' },
});
