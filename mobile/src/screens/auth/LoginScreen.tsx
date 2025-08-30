import React, { useState } from 'react';
import {
  View,
  StyleSheet,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
} from 'react-native';
import {
  TextInput,
  Button,
  Title,
  Paragraph,
  Card,
  ActivityIndicator,
  Snackbar,
} from 'react-native-paper';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigation } from '@react-navigation/native';
import { loginUser, clearError } from '../../store/slices/authSlice';
import { RootState, AppDispatch } from '../../store';

const LoginScreen: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  
  const dispatch = useDispatch<AppDispatch>();
  const navigation = useNavigation();
  const { isLoading, error } = useSelector((state: RootState) => state.auth);
  
  const handleLogin = async () => {
    if (!email.trim() || !password.trim()) {
      Alert.alert('Error', 'Please fill in all fields');
      return;
    }
    
    try {
      await dispatch(loginUser({ email: email.trim(), password })).unwrap();
      // Navigation will be handled by App.tsx based on auth state
    } catch (error) {
      // Error is handled by the reducer
    }
  };
  
  const navigateToRegister = () => {
    navigation.navigate('Register' as never);
  };
  
  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.content}>
          <Title style={styles.title}>Welcome to ClassBuddy</Title>
          <Paragraph style={styles.subtitle}>
            Your all-in-one college assistant
          </Paragraph>
          
          <Card style={styles.card}>
            <Card.Content>
              <TextInput
                label="Email"
                value={email}
                onChangeText={setEmail}
                keyboardType="email-address"
                autoCapitalize="none"
                autoComplete="email"
                style={styles.input}
                mode="outlined"
                disabled={isLoading}
              />
              
              <TextInput
                label="Password"
                value={password}
                onChangeText={setPassword}
                secureTextEntry={!showPassword}
                autoComplete="password"
                style={styles.input}
                mode="outlined"
                disabled={isLoading}
                right={
                  <TextInput.Icon
                    icon={showPassword ? 'eye-off' : 'eye'}
                    onPress={() => setShowPassword(!showPassword)}
                  />
                }
              />
              
              <Button
                mode="contained"
                onPress={handleLogin}
                style={styles.loginButton}
                disabled={isLoading}
                loading={isLoading}
              >
                {isLoading ? 'Signing In...' : 'Sign In'}
              </Button>
              
              <Button
                mode="text"
                onPress={navigateToRegister}
                style={styles.registerButton}
                disabled={isLoading}
              >
                Don't have an account? Sign Up
              </Button>
            </Card.Content>
          </Card>
        </View>
      </ScrollView>
      
      <Snackbar
        visible={!!error}
        onDismiss={() => dispatch(clearError())}
        duration={4000}
        action={{
          label: 'Dismiss',
          onPress: () => dispatch(clearError()),
        }}
      >
        {error}
      </Snackbar>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContainer: {
    flexGrow: 1,
    justifyContent: 'center',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    textAlign: 'center',
    marginBottom: 8,
    fontSize: 28,
    fontWeight: 'bold',
  },
  subtitle: {
    textAlign: 'center',
    marginBottom: 32,
    opacity: 0.7,
  },
  card: {
    padding: 16,
    elevation: 4,
  },
  input: {
    marginBottom: 16,
  },
  loginButton: {
    marginTop: 16,
    marginBottom: 8,
    paddingVertical: 8,
  },
  registerButton: {
    marginTop: 8,
  },
});

export default LoginScreen;
