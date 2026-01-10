import type { ReactNode } from "react";
import { View } from "react-native";

export interface ErrorBoundaryProps {
  children: ReactNode;
}

export function ErrorBoundary({ children }: ErrorBoundaryProps) {
  // TODO: Implement real error boundary logic
  return <View>{children}</View>;
}
