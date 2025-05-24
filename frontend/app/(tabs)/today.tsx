import { View } from "react-native"
import { Image, StyleSheet } from "react-native"
import { Text } from "react-native-paper"
import { Appbar } from "react-native-paper"
import { SafeAreaView } from "react-native-safe-area-context"

export default function TodaysOutfit() {
  const goBack = () => console.log("Went back")

  return (
    <View style={styles.view}>
      <Appbar.Header mode="large" style={styles.appBar}>
        <Appbar.BackAction onPress={goBack} />
      </Appbar.Header>
      <Image
        source={{
          uri: "https://i.pinimg.com/736x/b1/5f/2f/b15f2f2b23423e0d6e9159420670a934.jpg",
        }}
        style={styles.outfitImage}
      />

      <View style={styles.content}>
        <Text style={{ color: "#c4b2a1" }} variant="titleLarge">
          Today's Outfit
        </Text>
        <Text variant="bodyMedium">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </Text>
      </View>

      {/* <ParallaxScrollView
        headerBackgroundColor={{ light: "#A1CEDC", dark: "#1D3D47" }}
        headerImage={
          <Image
            source={{
              uri: "https://i.pinimg.com/736x/b1/5f/2f/b15f2f2b23423e0d6e9159420670a934.jpg",
            }}
            style={styles.outfitImage}
          />
        }
      >
        
      </ParallaxScrollView> */}
    </View>
  )
}

const styles = StyleSheet.create({
  view: {
    height: "100%",
  },
  outfitImage: {
    height: "50%",
    width: "100%",
  },
  appBar: {
    top: 0,
    left: 0,
    position: "absolute",
    zIndex: 100,
  },
  content: {
    padding: 12,
  },
})
