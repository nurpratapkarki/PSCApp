import { create } from 'zustand';
import { createJSONStorage, persist } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import type { LanguagePreference } from '../types/user.types';

interface SettingsState {
  // State
  language: LanguagePreference;
  notificationsEnabled: boolean;
  soundEnabled: boolean;
  darkMode: boolean;
  fontSize: 'small' | 'medium' | 'large';

  // Actions
  setLanguage: (language: LanguagePreference) => void;
  setNotificationsEnabled: (enabled: boolean) => void;
  setSoundEnabled: (enabled: boolean) => void;
  setDarkMode: (enabled: boolean) => void;
  setFontSize: (size: 'small' | 'medium' | 'large') => void;
  resetSettings: () => void;
}

const defaultSettings = {
  language: 'EN' as LanguagePreference,
  notificationsEnabled: true,
  soundEnabled: true,
  darkMode: false,
  fontSize: 'medium' as const,
};

export const useSettingsStore = create<SettingsState>()(
  persist(
    (set) => ({
      // Initial state
      ...defaultSettings,

      // Actions
      setLanguage: (language: LanguagePreference) => {
        set({ language });
      },

      setNotificationsEnabled: (enabled: boolean) => {
        set({ notificationsEnabled: enabled });
      },

      setSoundEnabled: (enabled: boolean) => {
        set({ soundEnabled: enabled });
      },

      setDarkMode: (enabled: boolean) => {
        set({ darkMode: enabled });
      },

      setFontSize: (size: 'small' | 'medium' | 'large') => {
        set({ fontSize: size });
      },

      resetSettings: () => {
        set(defaultSettings);
      },
    }),
    {
      name: 'settings-storage',
      storage: createJSONStorage(() => AsyncStorage),
    }
  )
);

// Selectors
export const selectLanguage = (state: SettingsState) => state.language;
export const selectNotificationsEnabled = (state: SettingsState) => state.notificationsEnabled;
export const selectSoundEnabled = (state: SettingsState) => state.soundEnabled;
export const selectDarkMode = (state: SettingsState) => state.darkMode;
export const selectFontSize = (state: SettingsState) => state.fontSize;

