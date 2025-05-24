import { MD3LightTheme } from "react-native-paper"

const theme = {
  ...MD3LightTheme, // or MD3DarkTheme
  roundness: 2,
  colors: {
    ...MD3LightTheme.colors,
    primary: "#3498db",
    secondary: "#f1c40f",
    tertiary: "#a1b2c3",
  },
  fonts: {
    ...MD3LightTheme.fonts,
    titleLarge: {
      fontSize: 30,
      fontWeight: 600,
    },
  },
}

export default theme
