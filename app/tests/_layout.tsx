import { Stack } from "expo-router";

export default function TestsLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen name="create" options={{ title: "Create Test" }} />
      <Stack.Screen name="history" options={{ title: "Test History" }} />
      <Stack.Screen name="[testId]/index" options={{ title: "Test Details" }} />
      <Stack.Screen name="[testId]/instructions" options={{ title: "Instructions" }} />
      <Stack.Screen name="[testId]/attempt" options={{ title: "Test", headerBackVisible: false }} />
      <Stack.Screen name="[testId]/results" options={{ title: "Results", headerBackVisible: false }} />
    </Stack>
  );
}

