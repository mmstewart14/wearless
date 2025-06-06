import React, { useState, useEffect } from "react";
import {
  View,
  StyleSheet,
  FlatList,
  Image,
  TouchableOpacity,
  Dimensions,
  ScrollView,
  RefreshControl,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { ThemedText } from "@/components/ThemedText";
import { ThemedView } from "@/components/ThemedView";
import { Colors } from "@/constants/Colors";
import { useColorScheme } from "@/hooks/useColorScheme";

// Mock outfit data - replace with actual API calls
const mockOutfits = [
  {
    id: "1",
    imageUrl:
      "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400&h=600&fit=crop",
    title: "Summer Casual",
    tags: ["casual", "summer", "comfortable"],
    likes: 24,
    height: 300,
  },
  {
    id: "2",
    imageUrl:
      "https://images.unsplash.com/photo-1445205170230-053b83016050?w=400&h=500&fit=crop",
    title: "Business Professional",
    tags: ["business", "professional", "formal"],
    likes: 18,
    height: 250,
  },
  {
    id: "3",
    imageUrl:
      "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400&h=650&fit=crop",
    title: "Evening Elegance",
    tags: ["evening", "elegant", "formal"],
    likes: 42,
    height: 350,
  },
  {
    id: "4",
    imageUrl:
      "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=400&h=550&fit=crop",
    title: "Weekend Vibes",
    tags: ["weekend", "relaxed", "casual"],
    likes: 31,
    height: 280,
  },
  {
    id: "5",
    imageUrl:
      "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=400&h=600&fit=crop",
    title: "Street Style",
    tags: ["street", "urban", "trendy"],
    likes: 56,
    height: 320,
  },
  {
    id: "6",
    imageUrl:
      "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&h=480&fit=crop",
    title: "Minimalist Chic",
    tags: ["minimalist", "chic", "modern"],
    likes: 29,
    height: 240,
  },
  {
    id: "7",
    imageUrl:
      "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400&h=580&fit=crop",
    title: "Boho Dreams",
    tags: ["boho", "artistic", "free-spirited"],
    likes: 37,
    height: 290,
  },
  {
    id: "8",
    imageUrl:
      "https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?w=400&h=520&fit=crop",
    title: "Classic Comfort",
    tags: ["classic", "comfortable", "timeless"],
    likes: 22,
    height: 260,
  },
];

interface Outfit {
  id: string;
  imageUrl: string;
  title: string;
  tags: string[];
  likes: number;
  height: number;
}

interface OutfitCardProps {
  outfit: Outfit;
  width: number;
  onPress: (outfit: Outfit) => void;
}

const OutfitCard: React.FC<OutfitCardProps> = ({ outfit, width, onPress }) => {
  const colorScheme = useColorScheme();
  const colors = Colors[colorScheme ?? "light"];

  return (
    <TouchableOpacity
      style={[styles.card, { width, backgroundColor: colors.background }]}
      onPress={() => onPress(outfit)}
      activeOpacity={0.9}
    >
      <Image
        source={{ uri: outfit.imageUrl }}
        style={[styles.cardImage, { height: outfit.height }]}
        resizeMode="cover"
      />
      <View style={styles.cardContent}>
        <ThemedText style={styles.cardTitle} numberOfLines={1}>
          {outfit.title}
        </ThemedText>
        <View style={styles.tagsContainer}>
          {outfit.tags.slice(0, 2).map((tag, index) => (
            <View
              key={index}
              style={[styles.tag, { backgroundColor: colors.tint + "20" }]}
            >
              <ThemedText style={[styles.tagText, { color: colors.tint }]}>
                {tag}
              </ThemedText>
            </View>
          ))}
        </View>
        <View style={styles.likesContainer}>
          <ThemedText style={styles.likesText}>♥ {outfit.likes}</ThemedText>
        </View>
      </View>
    </TouchableOpacity>
  );
};

export default function Outfits() {
  const colorScheme = useColorScheme();
  const colors = Colors[colorScheme ?? "light"];
  const [outfits, setOutfits] = useState<Outfit[]>(mockOutfits);
  const [refreshing, setRefreshing] = useState(false);
  const [selectedFilter, setSelectedFilter] = useState<string>("all");

  const screenWidth = Dimensions.get("window").width;
  const cardWidth = (screenWidth - 30) / 2; // 2 columns with padding

  const filters = ["all", "casual", "formal", "business", "evening", "street"];

  const filteredOutfits = outfits.filter(
    (outfit) => selectedFilter === "all" || outfit.tags.includes(selectedFilter)
  );

  const onRefresh = async () => {
    setRefreshing(true);
    // Simulate API call
    setTimeout(() => {
      setRefreshing(false);
    }, 1000);
  };

  const handleOutfitPress = (outfit: Outfit) => {
    console.log("Outfit pressed:", outfit.title);
    // Navigate to outfit detail screen
  };

  const renderOutfitCard = ({
    item,
    index,
  }: {
    item: Outfit;
    index: number;
  }) => (
    <OutfitCard outfit={item} width={cardWidth} onPress={handleOutfitPress} />
  );

  const renderFilterButton = (filter: string) => (
    <TouchableOpacity
      key={filter}
      style={[
        styles.filterButton,
        {
          backgroundColor:
            selectedFilter === filter ? colors.tint : colors.background,
          borderColor: colors.tint,
        },
      ]}
      onPress={() => setSelectedFilter(filter)}
    >
      <ThemedText
        style={[
          styles.filterText,
          {
            color: selectedFilter === filter ? colors.background : colors.tint,
          },
        ]}
      >
        {filter.charAt(0).toUpperCase() + filter.slice(1)}
      </ThemedText>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView
      style={[styles.container, { backgroundColor: colors.background }]}
    >
      <ThemedView style={styles.header}>
        <ThemedText type="title" style={styles.headerTitle}>
          Outfit Explorer
        </ThemedText>
        <ThemedText style={styles.headerSubtitle}>
          Discover your perfect style
        </ThemedText>
      </ThemedView>

      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        style={styles.filtersContainer}
        contentContainerStyle={styles.filtersContent}
      >
        {filters.map(renderFilterButton)}
      </ScrollView>

      <FlatList
        data={filteredOutfits}
        renderItem={renderOutfitCard}
        keyExtractor={(item) => item.id}
        numColumns={2}
        columnWrapperStyle={styles.row}
        contentContainerStyle={styles.listContainer}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
            tintColor={colors.tint}
          />
        }
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    paddingHorizontal: 20,
    paddingTop: 20,
    paddingBottom: 15,
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: "bold",
    marginBottom: 5,
  },
  headerSubtitle: {
    fontSize: 16,
    opacity: 0.7,
  },
  filtersContainer: {
    maxHeight: 50,
    marginBottom: 15,
  },
  filtersContent: {
    paddingHorizontal: 20,
    gap: 10,
  },
  filterButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    borderWidth: 1,
  },
  filterText: {
    fontSize: 14,
    fontWeight: "500",
  },
  listContainer: {
    paddingHorizontal: 10,
    paddingBottom: 100, // Account for tab bar
  },
  row: {
    justifyContent: "space-between",
    paddingHorizontal: 5,
  },
  card: {
    marginBottom: 15,
    borderRadius: 12,
    overflow: "hidden",
    elevation: 3,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
  },
  cardImage: {
    width: "100%",
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
  },
  cardContent: {
    padding: 12,
  },
  cardTitle: {
    fontSize: 16,
    fontWeight: "600",
    marginBottom: 8,
  },
  tagsContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 6,
    marginBottom: 8,
  },
  tag: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  tagText: {
    fontSize: 12,
    fontWeight: "500",
  },
  likesContainer: {
    flexDirection: "row",
    alignItems: "center",
  },
  likesText: {
    fontSize: 14,
    fontWeight: "500",
    opacity: 0.7,
  },
});
