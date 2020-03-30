import 'react-native-gesture-handler';
import React, { useState, useEffect, useMemo } from 'react';
import { StyleSheet, Text, View, StatusBar } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import { AuthContext } from './Context';

import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';

import LoadingScreen from './screens/LoadingScreen';
import ProfileScreen from './screens/ProfileScreen';
import FeedScreen from './screens/FeedScreen';
import SettingsScreen from './screens/SettingsScreen';

const AuthStack = createStackNavigator();
const FeedStack = createStackNavigator();
const Tabs = createBottomTabNavigator();

const App = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [userToken, setUserToken] = useState(null);

  const authContext = useMemo(() => {
    return {
      signIn: () => {
        setIsLoading(false);
        setUserToken('ABuddySandwichBud');
        console.log('Sign in called')
      },
      signUp: () => {
        setIsLoading(false);
        setUserToken('ABuddySandwichBud');
        console.log('Sign up called')
      },
      signOut: () => {
        setIsLoading(false);
        setUserToken(null);
        console.log('Sign out called')
      }
    }
  }, [])

  return (
    <AuthContext.Provider value={authContext}>
      <StatusBar hidden />
      <NavigationContainer>
        {userToken ? (
          <Tabs.Navigator>
            <Tabs.Screen name='Feed' component={FeedScreen} />
            <Tabs.Screen name='Squad Goals' component={FeedScreen} />
            <Tabs.Screen name='Profile' component={ProfileScreen} />
            <Tabs.Screen name='Settings' component={SettingsScreen} />
          </Tabs.Navigator>
        ) : (
            <AuthStack.Navigator>
              <AuthStack.Screen
                name='Login'
                component={LoginScreen}
              />
              <AuthStack.Screen
                name='Register'
                component={RegisterScreen}
              />
            </AuthStack.Navigator>
          )}

      </NavigationContainer>
    </AuthContext.Provider>
  );
}

export default App;