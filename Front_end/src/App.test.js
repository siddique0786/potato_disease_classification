// import { render, screen } from '@testing-library/react';
// import App from './App';

// test('renders learn react link', () => {
//   render(<App />);
//   const linkElement = screen.getByText(/learn react/i);
//   expect(linkElement).toBeInTheDocument();
// });
import { render, screen } from '@testing-library/react';
import { ImageUpload } from './home';

test('renders ImageUpload component', () => {
  render(<ImageUpload />);
  // You can now add assertions based on elements or text in your ImageUpload component
  // For example:
  const uploadText = screen.getByText(/Drag and drop an image of a potato plant leaf to process/i);
  expect(uploadText).toBeInTheDocument();
});
