import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button } from 'react-native';
import { AuthContext } from '../Context';

const SettingsScreen = ({ navigation }) => {
    const { signOut } = React.useContext(AuthContext);
    return (
        <View>
            <Text style={styles.headerText}>Account Settings</Text>
            <TouchableOpacity style={styles.button} onPress={signOut}>
                <Text style={styles.buttonText}>Change Account Name / Password</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button} onPress={signOut}>
                <Text style={styles.buttonText}>Sign Out</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.deleteButton} onPress={signOut}>
                <Text style={styles.buttonText}>Delete Account</Text>
            </TouchableOpacity>
        </View >
    );
}

const styles = StyleSheet.create({
    headerText: {
        fontSize: 20,
        textAlign: 'center'
    },
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
        marginTop: 10,
        height: 50,
        backgroundColor: 'skyblue',
        alignItems: 'center',
        justifyContent: 'center'
    },
    deleteButton: {
        marginTop: 10,
        height: 50,
        backgroundColor: 'red',
        alignItems: 'center',
        justifyContent: 'center'
    },
    buttonText: {
        fontSize: 20,
        color: 'white'
    }
});
export default SettingsScreen;