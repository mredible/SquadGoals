import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button, Image } from 'react-native';

const GoalCard = ({ navigation }) => {
    return (
        <View style={styles.outerContainer}>
            <View style={styles.container}>
                <View style={styles.header}>
                    <Image style={styles.avatar} source={require('../assets/icon.png')} />
                    <Text>Edward Fry</Text>
                </View>
                <View style={styles.image}>
                    <Text>My goal is to become a chess master</Text>
                </View>
                <View style={styles.buttons}>
                    <Button title='like' />
                    <Button title='comment' />
                    <Button title='Copy' />
                </View>
                <View>
                    <Text>Comments:</Text>
                </View>
            </View >
        </View>
    );
}

const styles = StyleSheet.create({
    outerContainer: {
        marginTop: 50,
        marginLeft: 10,
        marginRight: 10,
        backgroundColor: '#fff',
        alignItems: 'center',
        alignSelf: 'stretch',
    },
    header: {
        flexDirection: 'row',
        alignItems: 'center',
        alignSelf: 'stretch',
        flex: 0.1
    },
    container: {
        flex: 1,
        alignSelf: 'stretch',
        height: 400,
        margin: 10
    },
    buttons: {
        flexDirection: 'row',

        backgroundColor: 'white',
        alignSelf: 'stretch'
    },
    image: {
        backgroundColor: 'skyblue',
        flex: 1,
        alignSelf: 'stretch',
    },
    avatar: {
        height: 30,
        width: 30,
        marginRight: 10,
        borderRadius: 30
    }
});
export default GoalCard;