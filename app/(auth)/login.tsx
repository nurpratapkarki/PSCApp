import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, KeyboardAvoidingView, Platform } from 'react-native';
import { Text, Button, TextInput, Divider } from 'react-native-paper';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { Colors } from '../../constants/colors';
import { Spacing, BorderRadius } from '../../constants/typography';
import { useAuth } from '../../hooks/useAuth';

export default function LoginScreen() {
  const router = useRouter();
  const { login, devLogin, googleLogin, isLoading, error: authError } = useAuth();
  const [showDevLogin, setShowDevLogin] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);

  const handleGoogleLogin = async () => {
    setError(null);
    try {
      // TODO: Implement actual Google OAuth with expo-auth-session
      // For now, redirect to profile setup
      router.push('/(auth)/profile-setup');
    } catch (err) {
      setError('Google sign-in failed. Please try again.');
    }
  };

  const handleDevLogin = async () => {
    if (!email || !password) {
      setError('Please enter email and password');
      return;
    }
    setError(null);
    try {
      await devLogin(email, password);
      router.replace('/(tabs)');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed. Please check your credentials.');
    }
  };

  const handleEmailLogin = async () => {
    if (!email || !password) {
      setError('Please enter email and password');
      return;
    }
    setError(null);
    try {
      await login({ email, password });
      router.replace('/(tabs)');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed. Please check your credentials.');
    }
  };

  const displayError = error || authError;

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {/* Logo & Header */}
          <View style={styles.header}>
            <View style={styles.logoContainer}>
              <MaterialCommunityIcons name="school" size={60} color={Colors.white} />
            </View>
            <Text style={styles.appName}>PSC Exam Prep</Text>
            <Text style={styles.tagline}>नेपाल लोक सेवा आयोग परीक्षा तयारी</Text>
          </View>

          {/* Login Card */}
          <View style={styles.loginCard}>
            <Text style={styles.welcomeText}>Welcome Back!</Text>
            <Text style={styles.subText}>Sign in to continue your preparation</Text>

            {displayError && (
              <View style={styles.errorContainer}>
                <MaterialCommunityIcons name="alert-circle" size={20} color={Colors.error} />
                <Text style={styles.errorText}>{displayError}</Text>
              </View>
            )}

            {/* Google Sign In Button */}
            <Button
              mode="contained"
              onPress={handleGoogleLogin}
              loading={isLoading && !showDevLogin}
              disabled={isLoading}
              style={styles.googleButton}
              contentStyle={styles.buttonContent}
              icon={({ size, color }) => (
                <MaterialCommunityIcons name="google" size={size} color={color} />
              )}
            >
              Continue with Google
            </Button>

            <View style={styles.dividerContainer}>
              <Divider style={styles.divider} />
              <Text style={styles.dividerText}>or</Text>
              <Divider style={styles.divider} />
            </View>

            {/* Dev Login Toggle */}
            <Button
              mode="outlined"
              onPress={() => setShowDevLogin(!showDevLogin)}
              style={styles.devToggleButton}
              icon={showDevLogin ? 'chevron-up' : 'chevron-down'}
            >
              Developer Login
            </Button>

            {showDevLogin && (
              <View style={styles.devLoginForm}>
                <TextInput
                  label="Email"
                  value={email}
                  onChangeText={setEmail}
                  mode="outlined"
                  keyboardType="email-address"
                  autoCapitalize="none"
                  style={styles.input}
                  left={<TextInput.Icon icon="email" />}
                />
                <TextInput
                  label="Password"
                  value={password}
                  onChangeText={setPassword}
                  mode="outlined"
                  secureTextEntry
                  style={styles.input}
                  left={<TextInput.Icon icon="lock" />}
                />
                <Button
                  mode="contained"
                  onPress={handleDevLogin}
                  loading={isLoading && showDevLogin}
                  disabled={isLoading}
                  style={styles.loginButton}
                  contentStyle={styles.buttonContent}
                >
                  Sign In
                </Button>
              </View>
            )}
          </View>

          {/* Footer */}
          <View style={styles.footer}>
            <Text style={styles.footerText}>
              By continuing, you agree to our{' '}
              <Text style={styles.linkText}>Terms of Service</Text> and{' '}
              <Text style={styles.linkText}>Privacy Policy</Text>
            </Text>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.primary,
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: Spacing.xl,
  },
  header: {
    alignItems: 'center',
    paddingTop: Spacing['3xl'],
    paddingBottom: Spacing['2xl'],
  },
  logoContainer: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: Spacing.base,
  },
  appName: {
    fontSize: 28,
    fontWeight: '700',
    color: Colors.white,
    marginBottom: Spacing.xs,
  },
  tagline: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.8)',
  },
  loginCard: {
    backgroundColor: Colors.white,
    borderRadius: BorderRadius.xl,
    padding: Spacing.xl,
    elevation: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 12,
  },
  welcomeText: {
    fontSize: 24,
    fontWeight: '700',
    color: Colors.textPrimary,
    textAlign: 'center',
    marginBottom: Spacing.xs,
  },
  subText: {
    fontSize: 14,
    color: Colors.textSecondary,
    textAlign: 'center',
    marginBottom: Spacing.xl,
  },
  errorContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.errorLight,
    padding: Spacing.md,
    borderRadius: BorderRadius.md,
    marginBottom: Spacing.base,
  },
  errorText: {
    color: Colors.error,
    marginLeft: Spacing.sm,
    flex: 1,
  },
  googleButton: {
    backgroundColor: Colors.primary,
    borderRadius: BorderRadius.lg,
  },
  buttonContent: {
    paddingVertical: Spacing.sm,
  },
  dividerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: Spacing.xl,
  },
  divider: {
    flex: 1,
    backgroundColor: Colors.border,
  },
  dividerText: {
    marginHorizontal: Spacing.base,
    color: Colors.textTertiary,
  },
  devToggleButton: {
    borderColor: Colors.border,
  },
  devLoginForm: {
    marginTop: Spacing.base,
  },
  input: {
    marginBottom: Spacing.md,
    backgroundColor: Colors.white,
  },
  loginButton: {
    borderRadius: BorderRadius.lg,
    marginTop: Spacing.sm,
  },
  footer: {
    paddingVertical: Spacing['2xl'],
  },
  footerText: {
    fontSize: 12,
    color: 'rgba(255, 255, 255, 0.7)',
    textAlign: 'center',
    lineHeight: 18,
  },
  linkText: {
    color: Colors.white,
    textDecorationLine: 'underline',
  },
});
