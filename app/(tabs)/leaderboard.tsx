import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { Text, Card, Avatar, Chip, ActivityIndicator, SegmentedButtons } from 'react-native-paper';
import { SafeAreaView } from 'react-native-safe-area-context';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useApi } from '../../hooks/useApi';
import { Colors } from '../../constants/colors';
import { Spacing, BorderRadius } from '../../constants/typography';

interface LeaderboardEntry {
  rank: number;
  user: { id: number; username: string; full_name: string; avatar_url?: string };
  score: number;
  questions_answered: number;
  accuracy: number;
}

export default function LeaderboardScreen() {
  const [period, setPeriod] = useState<'weekly' | 'monthly' | 'all_time'>('weekly');
  const { data: leaderboard, status } = useApi<LeaderboardEntry[]>(`/api/leaderboard/?period=${period}`);

  const getMedalColor = (rank: number) => {
    if (rank === 1) return '#FFD700';
    if (rank === 2) return '#C0C0C0';
    if (rank === 3) return '#CD7F32';
    return Colors.textTertiary;
  };

  const TopThreeCard = ({ entry, position }: { entry: LeaderboardEntry; position: number }) => (
    <View style={[styles.topCard, position === 1 && styles.topCardFirst]}>
      <View style={[styles.medalBadge, { backgroundColor: getMedalColor(entry.rank) }]}>
        <Text style={styles.medalText}>{entry.rank}</Text>
      </View>
      <Avatar.Text size={position === 1 ? 64 : 52} label={entry.user.full_name.substring(0, 2).toUpperCase()} style={{ backgroundColor: Colors.primary }} />
      <Text style={styles.topName} numberOfLines={1}>{entry.user.full_name}</Text>
      <Text style={styles.topScore}>{entry.score.toLocaleString()} pts</Text>
      <View style={styles.topStats}>
        <Text style={styles.topStatText}>{entry.accuracy.toFixed(0)}% accuracy</Text>
      </View>
    </View>
  );

  const LeaderboardRow = ({ entry }: { entry: LeaderboardEntry }) => (
    <Card style={styles.rowCard}>
      <Card.Content style={styles.rowContent}>
        <Text style={styles.rankText}>{entry.rank}</Text>
        <Avatar.Text size={40} label={entry.user.full_name.substring(0, 2).toUpperCase()} style={{ backgroundColor: Colors.secondary }} />
        <View style={styles.rowInfo}>
          <Text style={styles.rowName}>{entry.user.full_name}</Text>
          <Text style={styles.rowSubtext}>{entry.questions_answered} questions • {entry.accuracy.toFixed(0)}%</Text>
        </View>
        <Text style={styles.rowScore}>{entry.score.toLocaleString()}</Text>
      </Card.Content>
    </Card>
  );

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <View style={styles.header}>
        <Text style={styles.title}>Leaderboard</Text>
        <Text style={styles.subtitle}>लिडरबोर्ड</Text>
      </View>

      <View style={styles.segmentContainer}>
        <SegmentedButtons
          value={period}
          onValueChange={(value) => setPeriod(value as any)}
          buttons={[
            { value: 'weekly', label: 'Weekly' },
            { value: 'monthly', label: 'Monthly' },
            { value: 'all_time', label: 'All Time' },
          ]}
          style={styles.segmentedButtons}
        />
      </View>

      {status === 'loading' ? (
        <View style={styles.loaderContainer}>
          <ActivityIndicator size="large" color={Colors.primary} />
        </View>
      ) : (
        <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
          {/* Top 3 */}
          {leaderboard && leaderboard.length >= 3 && (
            <View style={styles.topThreeContainer}>
              <TopThreeCard entry={leaderboard[1]} position={2} />
              <TopThreeCard entry={leaderboard[0]} position={1} />
              <TopThreeCard entry={leaderboard[2]} position={3} />
            </View>
          )}

          {/* Rest of leaderboard */}
          <View style={styles.listContainer}>
            {leaderboard?.slice(3).map((entry) => (
              <LeaderboardRow key={entry.user.id} entry={entry} />
            ))}
          </View>

          {(!leaderboard || leaderboard.length === 0) && (
            <View style={styles.emptyContainer}>
              <MaterialCommunityIcons name="trophy-outline" size={60} color={Colors.textTertiary} />
              <Text style={styles.emptyText}>No leaderboard data yet</Text>
              <Text style={styles.emptySubtext}>Start practicing to appear on the leaderboard!</Text>
            </View>
          )}
        </ScrollView>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Colors.background },
  header: { paddingHorizontal: Spacing.base, paddingTop: Spacing.md, paddingBottom: Spacing.sm },
  title: { fontSize: 28, fontWeight: '700', color: Colors.textPrimary },
  subtitle: { fontSize: 14, color: Colors.primary },
  segmentContainer: { paddingHorizontal: Spacing.base, marginBottom: Spacing.md },
  segmentedButtons: { backgroundColor: Colors.white },
  loaderContainer: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  scrollContent: { paddingHorizontal: Spacing.base, paddingBottom: Spacing['3xl'] },
  topThreeContainer: { flexDirection: 'row', justifyContent: 'center', alignItems: 'flex-end', marginBottom: Spacing.xl, gap: Spacing.sm },
  topCard: { alignItems: 'center', backgroundColor: Colors.white, borderRadius: BorderRadius.lg, padding: Spacing.md, width: 100, elevation: 2 },
  topCardFirst: { width: 120, paddingVertical: Spacing.lg, marginBottom: Spacing.md },
  medalBadge: { position: 'absolute', top: -10, width: 28, height: 28, borderRadius: 14, alignItems: 'center', justifyContent: 'center' },
  medalText: { color: Colors.white, fontWeight: '700', fontSize: 14 },
  topName: { fontSize: 13, fontWeight: '600', color: Colors.textPrimary, marginTop: Spacing.sm, textAlign: 'center' },
  topScore: { fontSize: 16, fontWeight: '700', color: Colors.primary },
  topStats: { marginTop: Spacing.xs },
  topStatText: { fontSize: 10, color: Colors.textSecondary },
  listContainer: { gap: Spacing.sm },
  rowCard: { backgroundColor: Colors.white, borderRadius: BorderRadius.md },
  rowContent: { flexDirection: 'row', alignItems: 'center' },
  rankText: { width: 30, fontSize: 16, fontWeight: '700', color: Colors.textSecondary, textAlign: 'center' },
  rowInfo: { flex: 1, marginLeft: Spacing.md },
  rowName: { fontSize: 15, fontWeight: '600', color: Colors.textPrimary },
  rowSubtext: { fontSize: 12, color: Colors.textSecondary },
  rowScore: { fontSize: 16, fontWeight: '700', color: Colors.primary },
  emptyContainer: { alignItems: 'center', paddingTop: Spacing['3xl'] },
  emptyText: { fontSize: 18, fontWeight: '600', color: Colors.textPrimary, marginTop: Spacing.base },
  emptySubtext: { fontSize: 14, color: Colors.textSecondary, textAlign: 'center' },
});

