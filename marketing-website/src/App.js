import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import Header from './components/Header';
import Hero from './components/Hero';
import Features from './components/Features';
import HowItWorks from './components/HowItWorks';
import SuccessStories from './components/SuccessStories';
import Statistics from './components/Statistics';
import Blog from './components/Blog';
import Download from './components/Download';
import Footer from './components/Footer';
import BlogPage from './pages/BlogPage';
import AdminBlog from './pages/AdminBlog';

function HomePage() {
  return (
    <>
      <Hero />
      <Features />
      <HowItWorks />
      <SuccessStories />
      <Statistics />
      <Blog />
      <Download />
    </>
  );
}

function App() {
  const { i18n } = useTranslation();

  React.useEffect(() => {
    document.dir = i18n.language === 'ar' ? 'rtl' : 'ltr';
  }, [i18n.language]);

  return (
    <Router>
      <div className="min-h-screen bg-white">
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/blog" element={<BlogPage />} />
          <Route path="/admin/blog" element={<AdminBlog />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;