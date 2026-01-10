import { Stack } from "expo-router";
import { PaperProvider, MD3LightTheme } from "react-native-paper";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { StatusBar } from "expo-status-bar";
import { Colors } from "../constants/colors";

// Custom theme for the app - Professional PSC Exam Prep Theme
const theme = {
  ...MD3LightTheme,
  colors: {
    ...MD3LightTheme.colors,
    primary: Colors.primary,
    onPrimary: Colors.textOnPrimary,
    primaryContainer: Colors.primaryLight,
    secondary: Colors.accent,
    onSecondary: Colors.textOnSecondary,
    secondaryContainer: Colors.accentLight,
    tertiary: Colors.secondary,
    background: Colors.background,
    surface: Colors.surface,
    surfaceVariant: Colors.surfaceVariant,
    error: Colors.error,
    onError: Colors.white,
    outline: Colors.border,
  },
  roundness: 12,
};

export default function RootLayout() {
  return (
    <SafeAreaProvider>
      <PaperProvider theme={theme}>
        <StatusBar style="dark" />
        <Stack
          screenOptions={{
            headerShown: false,
            headerStyle: {
              backgroundColor: Colors.primary,
            },
            headerTintColor: Colors.white,
            headerTitleStyle: {
              fontWeight: '600',
            },
            contentStyle: {
              backgroundColor: Colors.background,
            },
          }}
        >
          <Stack.Screen name="index" options={{ headerShown: false }} />
          <Stack.Screen name="(auth)" options={{ headerShown: false }} />
          <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
          <Stack.Screen name="practice" options={{ headerShown: true, title: "Practice" }} />
          <Stack.Screen name="tests" options={{ headerShown: true, title: "Tests" }} />
          <Stack.Screen name="contribute" options={{ headerShown: true, title: "Contribute" }} />
          <Stack.Screen name="notifications" options={{ headerShown: true, title: "Notifications" }} />
          <Stack.Screen name="profile" options={{ headerShown: true, title: "Profile" }} />
          <Stack.Screen name="community" options={{ headerShown: true, title: "Community" }} />
          <Stack.Screen name="report" options={{ headerShown: true, title: "Report" }} />
          <Stack.Screen name="modal" options={{ presentation: "modal" }} />
        </Stack>
      </PaperProvider>
    </SafeAreaProvider>
  );
}
