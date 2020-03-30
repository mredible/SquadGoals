import React from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button, ScrollView } from 'react-native';
import { AuthContext } from '../Context';

import GoalCard from '../components/GoalCard';

const FeedScreen = ({ navigation }) => {
    return (
        <View style={styles.container}>
            <View style={styles.header}>
                <Text style={styles.headerText}>This is your feed!</Text>
            </View>
            <ScrollView contentContainerStyle={styles.scrollContainer} >
                <GoalCard />
                <GoalCard />
                <GoalCard />
                <GoalCard />
                <GoalCard />
                <GoalCard />
                <GoalCard />
            </ScrollView>
        </View >
    );
}

const styles = StyleSheet.create({
    container: {
    },
    scrollContainer: {
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
        alignItems: 'center'
    },
    header: {
        alignItems: 'center'
    },
    headerText: {
        fontSize: 20
    }
});
export default FeedScreen;