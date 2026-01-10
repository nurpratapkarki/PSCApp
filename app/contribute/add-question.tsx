import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, TouchableOpacity, Alert, KeyboardAvoidingView, Platform } from 'react-native';
import { Stack, useRouter } from 'expo-router';
import { Card, Text, TextInput, Button, Chip, ActivityIndicator, RadioButton } from 'react-native-paper';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useApi } from '../../hooks/useApi';
import { Branch, Category } from '../../types/category.types';
import { Colors } from '../../constants/colors';
import { Spacing, BorderRadius } from '../../constants/typography';

interface AnswerOption {
  text: string;
  isCorrect: boolean;
}

export default function AddQuestionScreen() {
  const router = useRouter();
  const { data: branches, status: branchStatus } = useApi<Branch[]>('/api/branches/');
  const [selectedBranch, setSelectedBranch] = useState<Branch | null>(null);
  const { data: categories, status: categoryStatus } = useApi<Category[]>(selectedBranch ? `/api/categories/?branch=${selectedBranch.id}` : '', !selectedBranch);

  const [questionText, setQuestionText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<Category | null>(null);
  const [answers, setAnswers] = useState<AnswerOption[]>([
    { text: '', isCorrect: true },
    { text: '', isCorrect: false },
    { text: '', isCorrect: false },
    { text: '', isCorrect: false },
  ]);
  const [explanation, setExplanation] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const updateAnswer = (index: number, text: string) => {
    const newAnswers = [...answers];
    newAnswers[index].text = text;
    setAnswers(newAnswers);
  };

  const setCorrectAnswer = (index: number) => {
    const newAnswers = answers.map((a, i) => ({ ...a, isCorrect: i === index }));
    setAnswers(newAnswers);
  };

  const handleSubmit = async () => {
    if (!questionText.trim()) {
      Alert.alert('Missing Question', 'Please enter the question text.');
      return;
    }
    if (!selectedCategory) {
      Alert.alert('Missing Category', 'Please select a category.');
      return;
    }
    if (answers.some((a) => !a.text.trim())) {
      Alert.alert('Missing Answers', 'Please fill in all answer options.');
      return;
    }
    setIsSubmitting(true);
    // Simulate API call
    setTimeout(() => {
      setIsSubmitting(false);
      Alert.alert('Success!', 'Your question has been submitted for review.', [{ text: 'OK', onPress: () => router.back() }]);
    }, 1500);
  };

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <Stack.Screen options={{ headerShown: false }} />
      <KeyboardAvoidingView style={{ flex: 1 }} behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <MaterialCommunityIcons name="arrow-left" size={24} color={Colors.textPrimary} />
          </TouchableOpacity>
          <Text style={styles.headerTitle}>Add Question</Text>
          <View style={{ width: 44 }} />
        </View>

        <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          {/* Branch Selection */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Select Branch</Text>
              {branchStatus === 'loading' ? (
                <ActivityIndicator size="small" color={Colors.primary} />
              ) : (
                <View style={styles.chipRow}>
                  {branches?.map((branch) => (
                    <Chip key={branch.id} selected={selectedBranch?.id === branch.id} onPress={() => { setSelectedBranch(branch); setSelectedCategory(null); }} style={styles.chip} selectedColor={Colors.primary}>
                      {branch.name_en}
                    </Chip>
                  ))}
                </View>
              )}
            </Card.Content>
          </Card>

          {/* Category Selection */}
          {selectedBranch && (
            <Card style={styles.card}>
              <Card.Content>
                <Text style={styles.inputLabel}>Select Category</Text>
                {categoryStatus === 'loading' ? (
                  <ActivityIndicator size="small" color={Colors.primary} />
                ) : (
                  <View style={styles.chipRow}>
                    {categories?.slice(0, 8).map((cat) => (
                      <Chip key={cat.id} selected={selectedCategory?.id === cat.id} onPress={() => setSelectedCategory(cat)} style={styles.chip} selectedColor={Colors.primary}>
                        {cat.name_en}
                      </Chip>
                    ))}
                  </View>
                )}
              </Card.Content>
            </Card>
          )}

          {/* Question Text */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Question Text</Text>
              <TextInput mode="outlined" placeholder="Enter your question here..." value={questionText} onChangeText={setQuestionText} multiline numberOfLines={4} style={styles.textArea} outlineColor={Colors.border} activeOutlineColor={Colors.primary} />
            </Card.Content>
          </Card>

          {/* Answer Options */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Answer Options</Text>
              <Text style={styles.inputHint}>Tap the radio button to mark the correct answer</Text>
              {answers.map((answer, index) => (
                <View key={index} style={styles.answerRow}>
                  <RadioButton value={String(index)} status={answer.isCorrect ? 'checked' : 'unchecked'} onPress={() => setCorrectAnswer(index)} color={Colors.success} />
                  <TextInput mode="outlined" placeholder={`Option ${String.fromCharCode(65 + index)}`} value={answer.text} onChangeText={(text) => updateAnswer(index, text)} style={styles.answerInput} outlineColor={answer.isCorrect ? Colors.success : Colors.border} activeOutlineColor={answer.isCorrect ? Colors.success : Colors.primary} dense />
                </View>
              ))}
            </Card.Content>
          </Card>

          {/* Explanation */}
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.inputLabel}>Explanation (Optional)</Text>
              <TextInput mode="outlined" placeholder="Explain why this is the correct answer..." value={explanation} onChangeText={setExplanation} multiline numberOfLines={3} style={styles.textArea} outlineColor={Colors.border} activeOutlineColor={Colors.primary} />
            </Card.Content>
          </Card>
        </ScrollView>

        {/* Submit Button */}
        <View style={styles.bottomAction}>
          <Button mode="contained" icon="send" style={styles.submitButton} contentStyle={styles.submitButtonContent} labelStyle={styles.submitButtonLabel} onPress={handleSubmit} loading={isSubmitting} disabled={isSubmitting}>
            Submit for Review
          </Button>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', padding: Spacing.base },
  backButton: { width: 44, height: 44, borderRadius: 22, backgroundColor: Colors.white, alignItems: 'center', justifyContent: 'center', elevation: 2 },
  headerTitle: { fontSize: 20, fontWeight: '700', color: Colors.textPrimary },
  scrollContent: { padding: Spacing.base, paddingBottom: 100 },
  card: { backgroundColor: Colors.white, borderRadius: BorderRadius.xl, marginBottom: Spacing.lg, elevation: 2 },
  inputLabel: { fontSize: 16, fontWeight: '600', color: Colors.textPrimary, marginBottom: Spacing.sm },
  inputHint: { fontSize: 12, color: Colors.textSecondary, marginBottom: Spacing.md },
  chipRow: { flexDirection: 'row', flexWrap: 'wrap', gap: Spacing.xs },
  chip: { marginBottom: Spacing.xs },
  textArea: { backgroundColor: Colors.white },
  answerRow: { flexDirection: 'row', alignItems: 'center', marginBottom: Spacing.sm },
  answerInput: { flex: 1, backgroundColor: Colors.white },
  bottomAction: { backgroundColor: Colors.white, padding: Spacing.base, borderTopWidth: 1, borderTopColor: Colors.border },
  submitButton: { borderRadius: BorderRadius.lg },
  submitButtonContent: { paddingVertical: Spacing.sm },
  submitButtonLabel: { fontSize: 16, fontWeight: '700' },
});
