# Welcome to your Expo app 👋

This is an [Expo](https://expo.dev) project created with [`create-expo-app`](https://www.npmjs.com/package/create-expo-app).

## Get started

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   npx expo start
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

You can start developing by editing the files inside the **app** directory. This project uses [file-based routing](https://docs.expo.dev/router/introduction).

## Get a fresh project

When you're ready, run:

```bash
npm run reset-project
```

This command will move the starter code to the **app-example** directory and create a blank **app** directory where you can start developing.

## Learn more

To learn more about developing your project with Expo, look at the following resources:

- [Expo documentation](https://docs.expo.dev/): Learn fundamentals, or go into advanced topics with our [guides](https://docs.expo.dev/guides).
- [Learn Expo tutorial](https://docs.expo.dev/tutorial/introduction/): Follow a step-by-step tutorial where you'll create a project that runs on Android, iOS, and the web.

## Join the community

Join our community of developers creating universal apps.

- [Expo on GitHub](https://github.com/expo/expo): View our open source platform and contribute.
- [Discord community](https://chat.expo.dev): Chat with Expo users and ask questions.


## App Structure 
📱 PSC Exam App - React Native (Expo + TypeScript) Folder Structure
├── 📁 app/                                 # Expo Router file-based routing
│   ├── 📁 (auth)/                          # Auth group (no header)
│   │   ├── login.tsx                       # Google Sign In screen
│   │   ├── welcome.tsx                     # Onboarding/Welcome screen
│   │   └── profile-setup.tsx               # Initial branch/sub-branch selection
│   │
│   ├── 📁 (tabs)/                          # Bottom tab navigation
│   │   ├── _layout.tsx                     # Tab bar configuration
│   │   ├── index.tsx                       # 🏠 Home/Dashboard screen
│   │   ├── practice.tsx                    # 📝 Practice Mode screen
│   │   ├── tests.tsx                       # 🎯 Mock Tests listing
│   │   ├── community.tsx                   # 👥 Community/Leaderboard
│   │   └── profile.tsx                     # 👤 User Profile screen
│   │
│   ├── 📁 practice/                        # Practice module screens
│   │   ├── categories.tsx                  # Category selection
│   │   ├── [categoryId]/                   
│   │   │   ├── index.tsx                   # Questions list for category
│   │   │   └── question.tsx                # Individual question view
│   │   └── results.tsx                     # Practice session results
│   │
│   ├── 📁 tests/                           # Mock test module screens
│   │   ├── [testId]/
│   │   │   ├── index.tsx                   # Test details/preview
│   │   │   ├── instructions.tsx            # Pre-test instructions
│   │   │   ├── attempt.tsx                 # Active test screen
│   │   │   └── results.tsx                 # Test results with analysis
│   │   ├── create.tsx                      # Create custom test
│   │   └── history.tsx                     # User's test history
│   │
│   ├── 📁 contribute/                      # Contribution module
│   │   ├── index.tsx                       # Contribution dashboard
│   │   ├── add-question.tsx                # Question submission form
│   │   ├── my-contributions.tsx            # User's contributions list
│   │   └── [questionId]/
│   │       └── edit.tsx                    # Edit pending question
│   │
│   ├── 📁 community/                       # Community features
│   │   ├── leaderboard.tsx                 # Global leaderboard
│   │   ├── top-contributors.tsx            # Monthly top contributors
│   │   ├── live-feed.tsx                   # Real-time activity feed
│   │   └── stats.tsx                       # Platform statistics
│   │
│   ├── 📁 profile/                         # Profile & settings
│   │   ├── edit.tsx                        # Edit profile
│   │   ├── settings.tsx                    # App settings
│   │   ├── statistics.tsx                  # Personal stats & badges
│   │   ├── collections.tsx                 # Study collections
│   │   ├── [collectionId]/
│   │   │   └── index.tsx                   # Collection details
│   │   └── preferences.tsx                 # Language, notifications
│   │
│   ├── 📁 notifications/                   
│   │   └── index.tsx                       # Notifications list
│   │
│   ├── 📁 report/                          
│   │   └── [questionId].tsx                # Report question form
│   │
│   ├── _layout.tsx                         # Root layout with providers
│   ├── +not-found.tsx                      # 404 screen
│   └── modal.tsx                           # Example modal screen
│
├── 📁 components/                          # Reusable components
│   ├── 📁 ui/                              # Basic UI components
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   ├── Checkbox.tsx
│   │   ├── RadioButton.tsx
│   │   ├── Badge.tsx
│   │   ├── ProgressBar.tsx
│   │   ├── Loader.tsx
│   │   ├── Avatar.tsx
│   │   ├── Chip.tsx
│   │   └── Modal.tsx
│   │
│   ├── 📁 question/                        # Question-related components
│   │   ├── QuestionCard.tsx                # Single question display
│   │   ├── AnswerOption.tsx                # MCQ answer choice
│   │   ├── QuestionTimer.tsx               # Timer component
│   │   ├── QuestionNavigator.tsx           # Question grid navigation
│   │   ├── ExplanationView.tsx             # Answer explanation
│   │   └── QuestionForm.tsx                # Add/edit question form
│   │
│   ├── 📁 test/                            # Test-related components
│   │   ├── TestCard.tsx                    # Mock test card
│   │   ├── TestTimer.tsx                   # Test countdown timer
│   │   ├── TestProgress.tsx                # Progress indicator
│   │   ├── TestSubmitDialog.tsx            # Submit confirmation
│   │   └── ResultsBreakdown.tsx            # Score breakdown charts
│   │
│   ├── 📁 category/
│   │   ├── CategoryCard.tsx                # Category selection card
│   │   ├── CategoryIcon.tsx                # Category icon display
│   │   └── CategoryFilter.tsx              # Filter by category
│   │
│   ├── 📁 leaderboard/
│   │   ├── LeaderboardItem.tsx             # Single rank entry
│   │   ├── RankBadge.tsx                   # Rank medal/badge
│   │   └── LeaderboardFilters.tsx          # Time period filters
│   │
│   ├── 📁 profile/
│   │   ├── StatCard.tsx                    # Statistics card
│   │   ├── BadgeDisplay.tsx                # Achievement badge
│   │   ├── StreakIndicator.tsx             # Streak counter
│   │   └── ProgressChart.tsx               # Category-wise progress
│   │
│   ├── 📁 contribution/
│   │   ├── ContributionCard.tsx            # Contribution status card
│   │   └── ContributionStats.tsx           # User contribution stats
│   │
│   ├── 📁 navigation/
│   │   ├── TabBar.tsx                      # Custom tab bar
│   │   ├── Header.tsx                      # Custom header
│   │   └── DrawerContent.tsx               # Drawer menu (if needed)
│   │
│   └── 📁 common/
│       ├── EmptyState.tsx                  # No data placeholder
│       ├── ErrorBoundary.tsx               # Error handling
│       ├── LanguageToggle.tsx              # EN/NP switcher
│       ├── SearchBar.tsx                   # Search input
│       └── FilterChips.tsx                 # Filter tags
│
├── 📁 hooks/                               # Custom React hooks
│   ├── useAuth.ts                          # Authentication state
│   ├── useQuestion.ts                      # Question operations
│   ├── useTest.ts                          # Test operations
│   ├── useTimer.ts                         # Timer logic
│   ├── useLeaderboard.ts                   # Leaderboard data
│   ├── useNotifications.ts                 # Notification handling
│   ├── useLanguage.ts                      # i18n language switching
│   ├── useTheme.ts                         # Theme management
│   └── useDebounce.ts                      # Debounce utility
│
├── 📁 services/                            # API & external services
│   ├── 📁 api/                             # API client
│   │   ├── client.ts                       # Axios instance config
│   │   ├── auth.ts                         # Auth endpoints
│   │   ├── questions.ts                    # Question CRUD
│   │   ├── tests.ts                        # Test endpoints
│   │   ├── contributions.ts                # Contribution endpoints
│   │   ├── leaderboard.ts                  # Leaderboard endpoints
│   │   ├── profile.ts                      # Profile endpoints
│   │   └── stats.ts                        # Statistics endpoints
│   │
│   ├── auth/
│   │   └── google.ts                       # Google OAuth integration
│   │
│   └── storage/
│       └── asyncStorage.ts                 # Local storage utilities
│
├── 📁 store/                               # State management (Redux/Zustand)
│   ├── 📁 slices/                          # Redux slices (or Zustand stores)
│   │   ├── authSlice.ts                    # Auth state
│   │   ├── questionSlice.ts                # Questions state
│   │   ├── testSlice.ts                    # Tests state
│   │   ├── userSlice.ts                    # User data
│   │   └── settingsSlice.ts                # App settings
│   │
│   └── index.ts                            # Store configuration
│
├── 📁 utils/                               # Utility functions
│   ├── validation.ts                       # Form validation
│   ├── formatting.ts                       # Date, number formatting
│   ├── timer.ts                            # Timer utilities
│   ├── scoring.ts                          # Score calculation
│   ├── constants.ts                        # App constants
│   └── helpers.ts                          # General helpers
│
├── 📁 types/                               # TypeScript types
│   ├── index.ts                            # Main type exports
│   ├── auth.types.ts                       # Authentication types
│   ├── question.types.ts                   # Question & Answer types
│   ├── test.types.ts                       # Test types
│   ├── user.types.ts                       # User & Profile types
│   ├── category.types.ts                   # Category types
│   ├── contribution.types.ts               # Contribution types
│   └── api.types.ts                        # API response types
│
├── 📁 constants/                           # App constants
│   ├── colors.ts                           # Color palette
│   ├── typography.ts                       # Font styles
│   ├── spacing.ts                          # Spacing scale
│   ├── routes.ts                           # Route names
│   └── config.ts                           # App config
│
├── 📁 locales/                             # Internationalization
│   ├── en.json                             # English translations
│   ├── np.json                             # Nepali translations
│   └── index.ts                            # i18n configuration
│
├── 📁 assets/                              # Static assets
│   ├── 📁 images/
│   │   ├── logo.png
│   │   ├── onboarding/
│   │   └── badges/
│   │
│   ├── 📁 icons/
│   │   ├── categories/
│   │   └── badges/
│   │
│   └── 📁 fonts/
│       └── (custom fonts if any)
│
├── 📁 config/                              # Configuration files
│   ├── api.config.ts                       # API base URLs, endpoints
│   ├── auth.config.ts                      # Auth provider config
│   └── app.config.ts                       # General app config
│
├── 📄 .env                                 # Environment variables
├── 📄 .env.example                         # Example env file
├── 📄 app.json                             # Expo configuration
├── 📄 babel.config.js                      # Babel config
├── 📄 tsconfig.json                        # TypeScript config
├── 📄 package.json                         # Dependencies
└── 📄 README.md                            # Project documentation


# ============================================================================
# SCREEN COUNT SUMMARY
# ============================================================================

📱 TOTAL SCREENS: ~35-40 screens

## Authentication Flow (3 screens)
✓ Welcome/Onboarding
✓ Login (Google Sign In)
✓ Profile Setup (Branch/Sub-branch selection)

## Main Tab Screens (5 screens)
✓ Home/Dashboard
✓ Practice Mode
✓ Mock Tests
✓ Community
✓ Profile

## Practice Module (4 screens)
✓ Category Selection
✓ Questions List
✓ Question View (with answers)
✓ Practice Results

## Mock Test Module (5 screens)
✓ Test Listing
✓ Test Details/Preview
✓ Pre-test Instructions
✓ Active Test (with timer)
✓ Test Results & Analysis
✓ Test History

## Contribution Module (4 screens)
✓ Contribution Dashboard
✓ Add New Question
✓ My Contributions List
✓ Edit Question

## Community Module (4 screens)
✓ Leaderboard
✓ Top Contributors
✓ Live Activity Feed
✓ Platform Statistics

## Profile & Settings (6 screens)
✓ Profile View
✓ Edit Profile
✓ Settings
✓ Statistics & Badges
✓ Study Collections
✓ Collection Details
✓ Preferences

## Additional Screens (4 screens)
✓ Notifications
✓ Report Question
✓ Search Results
✓ 404 Not Found


# ============================================================================
# KEY TECHNICAL DECISIONS
# ============================================================================

🎯 ROUTING: Expo Router (file-based)
   - Simpler than React Navigation manual setup
   - Type-safe navigation
   - Automatic deep linking

🎨 STYLING: NativeWind (Tailwind for RN) or StyleSheet
   - Consistent with web styling
   - Fast development

🔄 STATE: Redux Toolkit or Zustand
   - Redux Toolkit: More enterprise, better DevTools
   - Zustand: Lighter, simpler API

🌐 API: Axios with Interceptors
   - Token refresh handling
   - Request/response logging

🔔 NOTIFICATIONS: Expo Notifications
   - Push notifications for streaks, approvals, etc.

🎨 UI LIBRARY OPTIONS:
   - React Native Paper (Material Design)
   - NativeBase
   - Custom components (full control)

📊 CHARTS: react-native-chart-kit or Victory Native
   - For progress charts, test analytics


# ============================================================================
# TODO: Initial Setup Commands
# ============================================================================



# 2. Install essential dependencies
npm install @react-navigation/native
npm install axios
npm install @react-native-async-storage/async-storage
npm install expo-google-app-auth
npm install @reduxjs/toolkit react-redux  # If using Redux
npm install zustand  # If using Zustand
npm install i18next react-i18next
npm install expo-notifications

# 3. Install UI library (choose one)
npm install react-native-paper
# OR
npm install native-base

# 4. Install dev dependencies
npm install --save-dev @types/react @types/react-native