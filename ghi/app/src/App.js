import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import ShoeForm from './ShoeForm';
import ShoeList from './ShoeList';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route index element={<MainPage />} />
          <Route path="shoes">
            <Route path="new" element={<ShoeForm />} />
            <Route path="" element={<ShoeList />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
