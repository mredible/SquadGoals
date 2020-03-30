import React, { useContext } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, KeyboardAvoidingView } from 'react-native';
import { AuthContext } from '../Context';

const RegisterScreen = () => {
    const { signUp } = useContext(AuthContext);
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
            <TextInput
                style={styles.input}
                placeholder='Confirm Password'
                secureTextEntry
            />
            <Text>Agree To our Terms and conditions</Text>
            <TouchableOpacity
                style={styles.button}
                onPress={signUp}
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
export default RegisterScreen;