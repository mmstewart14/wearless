# Welcome to your Expo app 👋

This is an [Expo](https://expo.dev) project created with [`create-expo-app`](https://www.npmjs.com/package/create-expo-app).

## Get started

1. Install dependencies

   ```bash
   npm install --legacy-peer-deps
   ```

2. Start the app

   ```bash
    npx expo start
   ```

## Expo

1. Remedying with Expo Dependencies

If you see this message in the output of `npx expo start`

```bash
The following packages should be updated for best compatibility with the installed expo version"
```

run the following command:

```bash
npx expo install --fix -- --legacy-peer-deps
```
