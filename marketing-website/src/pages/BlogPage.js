import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { Calendar, User, ArrowRight } from 'lucide-react';

const BlogPage = () => {
  const { t } = useTranslation();
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    // Load articles from localStorage
    const savedArticles = localStorage.getItem('pizoo_blog_articles');
    if (savedArticles) {
      setArticles(JSON.parse(savedArticles));
    } else {
      // Default articles
      const defaultArticles = [
        {
          id: 1,
          title: '10 Tips for Creating the Perfect Dating Profile',
          content: 'Creating a standout dating profile is essential to attract the right matches. Here are 10 expert tips to help you succeed...',
          excerpt: 'Learn how to make your profile stand out and attract the right matches with these expert tips.',
          author: 'Pizoo Team',
          date: new Date().toISOString(),
          category: 'Dating Tips',
          image: 'https://images.unsplash.com/photo-1607529378676-a20456ee2f6b?w=800',
        },
        {
          id: 2,
          title: 'First Date Ideas That Will Impress',
          content: 'Looking for unique first date ideas? Check out these creative suggestions that are sure to leave a lasting impression...',
          excerpt: 'Creative and memorable first date ideas that go beyond dinner and a movie.',
          author: 'Dating Experts',
          date: new Date().toISOString(),
          category: 'Date Ideas',
          image: 'https://images.unsplash.com/photo-1546961329-78bef0414d7c?w=800',
        },
        {
          id: 3,
          title: 'How to Keep the Conversation Going',
          content: 'Struggling with what to say? These conversation starters and tips will help you connect on a deeper level...',
          excerpt: 'Master the art of conversation with these proven techniques and tips.',
          author: 'Relationship Coach',
          date: new Date().toISOString(),
          category: 'Communication',
          image: 'https://images.unsplash.com/photo-1540222797359-e9b786124d4b?w=800',
        },
      ];
      setArticles(defaultArticles);
      localStorage.setItem('pizoo_blog_articles', JSON.stringify(defaultArticles));
    }
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 pt-24 pb-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold mb-4 gradient-text">{t('blog.title')}</h1>
          <p className="text-xl text-gray-600">{t('blog.subtitle')}</p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {articles.map((article) => (
            <article
              key={article.id}
              className="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition transform hover:-translate-y-2"
            >
              <img src={article.image} alt={article.title} className="w-full h-48 object-cover" />
              <div className="p-6">
                <div className="flex items-center text-sm text-gray-500 mb-3">
                  <Calendar className="w-4 h-4 mr-2" />
                  {new Date(article.date).toLocaleDateString()}
                  <span className="mx-2">•</span>
                  <span className="text-primary-500 font-medium">{article.category}</span>
                </div>
                <h2 className="text-2xl font-bold mb-3 text-gray-900">{article.title}</h2>
                <p className="text-gray-600 mb-4">{article.excerpt}</p>
                <div className="flex items-center justify-between">
                  <div className="flex items-center text-sm text-gray-500">
                    <User className="w-4 h-4 mr-2" />
                    {article.author}
                  </div>
                  <button className="text-primary-500 font-semibold hover:text-primary-600 transition flex items-center">
                    {t('blog.readMore')}
                    <ArrowRight className="w-4 h-4 ml-2" />
                  </button>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </div>
  );
};

export default BlogPage;