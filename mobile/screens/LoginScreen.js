import React, { useContext } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, KeyboardAvoidingView } from 'react-native';
import { AuthContext } from '../Context';

const LoginScreen = ({ navigation }) => {
    const { signIn } = useContext(AuthContext);
    return (
        <KeyboardAvoidingView behavior='padding' style={styles.container}>
            <Text>Sign in to Squad Goals</Text>
            <TextInput
                style={styles.input}
                placeholder='Email/Username'
                autoCorrect={false}
            />
            <TextInput
                style={styles.input}
                placeholder='Password'
                secureTextEntry
            />
            <TouchableOpacity
                style={styles.button}
                onPress={signIn}
            >
                <Text>Sign in</Text>
            </TouchableOpacity>
            <TouchableOpacity
                style={styles.button}
                onPress={() => navigation.push('Register')}
            >
                <Text>Register</Text>
            </TouchableOpacity>
        </KeyboardAvoidingView>
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
export default LoginScreen;