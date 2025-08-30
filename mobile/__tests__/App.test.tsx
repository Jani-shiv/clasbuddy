import React from 'react';
import {render} from '@testing-library/react-native';
import App from '../App';

describe('App', () => {
  test('renders correctly', () => {
    const {getByText} = render(<App />);
    // This is a basic test - in a real app, you'd test specific components
    expect(getByText).toBeDefined();
  });
});
