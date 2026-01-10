const DEFAULT_API_BASE_URL = "http://localhost:8000";

export const API_BASE_URL =
  process.env.EXPO_PUBLIC_API_BASE_URL ?? DEFAULT_API_BASE_URL;

export const API_ENDPOINTS = {
	auth: {
	  user: "/api/auth/user/",
	  devLogin: "/api/auth/dev-login/",
	  login: "/api/auth/login/",
	  logout: "/api/auth/logout/",
	  registration: "/api/auth/registration/",
	  googleLogin: "/api/auth/google/",
	  tokenObtainPair: "/token/",
	  tokenRefresh: "/token/refresh/",
	  tokenBlacklist: "/token/blacklist/",
	},
	branches: {
	  list: "/api/branches/",
	  subBranches: "/api/sub-branches/",
	  categories: "/api/categories/",
	},
	questions: {
	  list: "/api/questions/",
	  reports: "/api/reports/",
	},
	mockTests: {
	  list: "/api/mock-tests/",
	  generate: "/api/mock-tests/generate/",
	},
	attempts: {
	  list: "/api/attempts/",
	  start: "/api/attempts/start/",
	  detail: (id: number | string) => `/api/attempts/${id}/`,
	  submit: (id: number | string) => `/api/attempts/${id}/submit/`,
	  results: (id: number | string) => `/api/attempts/${id}/results/`,
	},
	answers: {
	  list: "/api/answers/",
	  detail: (id: number | string) => `/api/answers/${id}/`,
	},
	analytics: {
	  contributions: "/api/contributions/",
	  dailyActivity: "/api/daily-activity/",
	},
	stats: {
	  platform: "/api/platform-stats/",
	  statistics: "/api/statistics/",
	  statisticsMe: "/api/statistics/me/",
	  progress: "/api/progress/",
	  collections: "/api/collections/",
	  leaderboard: "/api/leaderboard/",
	},
	notifications: {
	  list: "/api/notifications/",
	  markRead: (id: number | string) => `/api/notifications/${id}/read/`,
	  markAllRead: "/api/notifications/read-all/",
	  unreadCount: "/api/notifications/unread/",
	},
	settings: {
	  list: "/api/settings/",
	  detail: (key: string) => `/api/settings/${encodeURIComponent(key)}/`,
	},
	timeConfigs: {
	  list: "/api/time-configs/",
	},
	} as const;
