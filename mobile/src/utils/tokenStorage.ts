import Keychain from 'react-native-keychain';

interface StoredTokens {
  accessToken: string;
  refreshToken?: string;
}

const TOKEN_SERVICE = 'ClassBuddyTokens';

export const setTokens = async (accessToken: string, refreshToken?: string): Promise<void> => {
  try {
    const tokens: StoredTokens = {
      accessToken,
      ...(refreshToken && { refreshToken }),
    };
    
    await Keychain.setInternetCredentials(
      TOKEN_SERVICE,
      'tokens',
      JSON.stringify(tokens)
    );
  } catch (error) {
    console.error('Error storing tokens:', error);
    throw error;
  }
};

export const getStoredTokens = async (): Promise<StoredTokens | null> => {
  try {
    const credentials = await Keychain.getInternetCredentials(TOKEN_SERVICE);
    
    if (credentials && credentials.password) {
      return JSON.parse(credentials.password) as StoredTokens;
    }
    
    return null;
  } catch (error) {
    console.error('Error retrieving tokens:', error);
    return null;
  }
};

export const clearTokens = async (): Promise<void> => {
  try {
    await Keychain.resetInternetCredentials(TOKEN_SERVICE);
  } catch (error) {
    console.error('Error clearing tokens:', error);
    throw error;
  }
};

export const hasStoredTokens = async (): Promise<boolean> => {
  try {
    const tokens = await getStoredTokens();
    return tokens !== null && !!tokens.accessToken;
  } catch (error) {
    console.error('Error checking stored tokens:', error);
    return false;
  }
};
