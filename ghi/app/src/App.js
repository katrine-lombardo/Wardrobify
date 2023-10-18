import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import ShoeForm from './ShoeForm';
import ShoeList from './ShoeList';
import HatForm from "./HatForm"
import HatList from "./HatList"


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
          <Route path="hats/new" element={<HatForm />} />
          <Route path="hats" element={<HatList />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
