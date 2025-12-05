import React from 'react';
import { useTranslation } from 'react-i18next';
import { Heart } from 'lucide-react';

const SuccessStories = () => {
  const { t } = useTranslation();

  const stories = [
    {
      image: 'https://images.unsplash.com/photo-1506277886164-e25aa3f4ef7f?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwyfHxzbWlsaW5nJTIwcGVyc29ufGVufDB8fHx8MTc2NDkyNTg4N3ww&ixlib=rb-4.1.0&q=85',
      name: 'Sarah & James',
      text: 'We met on Pizoo 6 months ago and now we\'re engaged! The smart matching feature really works. We had so much in common from the start.',
    },
    {
      image: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwzfHxzbWlsaW5nJTIwcGVyc29ufGVufDB8fHx8MTc2NDkyNTg4N3ww&ixlib=rb-4.1.0&q=85',
      name: 'Maria & David',
      text: 'I never thought I\'d find love online, but Pizoo changed my mind. The video calls helped us connect before meeting in person.',
    },
    {
      image: 'https://images.unsplash.com/photo-1521511189395-b82252213754?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHw0fHxkaXZlcnNlJTIwcGVvcGxlJTIwcG9ydHJhaXR8ZW58MHx8fHwxNzY0OTI1ODYzfDA&ixlib=rb-4.1.0&q=85',
      name: 'Emma & Alex',
      text: 'Best decision ever! We matched on Pizoo and have been inseparable since. Thank you for bringing us together!',
    },
  ];

  return (
    <section className="py-20 bg-gradient-to-br from-primary-50 to-secondary-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16 animate-fade-in">
          <h2 className="text-4xl md:text-5xl font-bold mb-4 gradient-text">
            {t('success.title')}
          </h2>
          <p className="text-xl text-gray-600">
            {t('success.subtitle')}
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {stories.map((story, index) => (
            <div
              key={index}
              className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition transform hover:-translate-y-2 animate-slide-up"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className="flex items-center mb-4">
                <img src={story.image} alt={story.name} className="w-16 h-16 rounded-full object-cover" />
                <div className="ml-4">
                  <h3 className="font-bold text-lg text-gray-900">{story.name}</h3>
                  <div className="flex items-center">
                    {[...Array(5)].map((_, i) => (
                      <Heart key={i} className="w-4 h-4 text-primary-500 fill-current" />
                    ))}
                  </div>
                </div>
              </div>
              <p className="text-gray-600 leading-relaxed italic">"{story.text}"</p>
            </div>
          ))}
        </div>

        <div className="text-center mt-12">
          <button className="text-primary-500 font-semibold hover:text-primary-600 transition">
            {t('success.readMore')} →
          </button>
        </div>
      </div>
    </section>
  );
};

export default SuccessStories;