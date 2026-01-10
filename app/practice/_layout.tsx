import { Stack } from "expo-router";

export default function PracticeLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen name="categories" options={{ title: "Select Category" }} />
      <Stack.Screen name="[categoryId]/index" options={{ title: "Practice Setup" }} />
      <Stack.Screen name="[categoryId]/question" options={{ title: "Practice", headerBackVisible: false }} />
      <Stack.Screen name="results" options={{ title: "Practice Results", headerBackVisible: false }} />
    </Stack>
  );
}

