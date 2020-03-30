import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button, Image } from 'react-native';

const ProfileScreen = ({ navigation }) => {
    return (
        <View>
            <Text>Your profile</Text>
            <Image source={require('../assets/icon.png')} />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    input: {
        borderWidth: 1,
        width: 200,
        marginTop: 10,
        padding: 5,
    },
    button: {
        backgroundColor: 'skyblue',
        width: 200,
        height: 30,
        marginTop: 10
    }
});
export default ProfileScreen;