import { Redirect } from "expo-router";

export default function Index() {
  // Redirect to the main tabs layout
  // In a real app, you'd check authentication state here
  // and redirect to (auth)/welcome or (tabs) accordingly
  return <Redirect href="/(tabs)" />;
}
