import React from 'react';
import { useTranslation } from 'react-i18next';
import { Heart, Users, Globe } from 'lucide-react';

const Hero = () => {
  const { t } = useTranslation();

  const openApp = () => {
    window.open('https://pizoo-debug.preview.emergentagent.com', '_blank');
  };

  return (
    <section id="home" className="pt-24 pb-20 gradient-bg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-white animate-fade-in">
            <h1 className="text-5xl md:text-6xl font-bold mb-6 leading-tight">
              {t('hero.title')}
            </h1>
            <p className="text-xl mb-8 text-white/90">
              {t('hero.subtitle')}
            </p>
            <button
              onClick={openApp}
              className="bg-white text-primary-500 px-8 py-4 rounded-full text-lg font-semibold hover:shadow-2xl transition transform hover:scale-105"
            >
              {t('hero.cta')}
            </button>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-6 mt-12">
              <div>
                <div className="flex items-center space-x-2 mb-2">
                  <Users className="w-6 h-6" />
                  <h3 className="text-2xl font-bold">{t('hero.stats.users')}</h3>
                </div>
              </div>
              <div>
                <div className="flex items-center space-x-2 mb-2">
                  <Heart className="w-6 h-6" />
                  <h3 className="text-2xl font-bold">{t('hero.stats.matches')}</h3>
                </div>
              </div>
              <div>
                <div className="flex items-center space-x-2 mb-2">
                  <Globe className="w-6 h-6" />
                  <h3 className="text-2xl font-bold">{t('hero.stats.countries')}</h3>
                </div>
              </div>
            </div>
          </div>

          {/* Right Content - Images */}
          <div className="relative animate-slide-up">
            <div className="grid grid-cols-2 gap-4">
              <img
                src="https://images.unsplash.com/photo-1546961329-78bef0414d7c?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwxfHx5b3VuZyUyMGFkdWx0JTIwcG9ydHJhaXR8ZW58MHx8fHwxNzY0OTI1ODc4fDA&ixlib=rb-4.1.0&q=85&w=400"
                alt="Pizoo User 1"
                className="rounded-2xl shadow-2xl w-full h-64 object-cover"
                loading="lazy"
              />
              <img
                src="https://images.unsplash.com/photo-1540222797359-e9b786124d4b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwyfHx5b3VuZyUyMGFkdWx0JTIwcG9ydHJhaXR8ZW58MHx8fHwxNzY0OTI1ODc4fDA&ixlib=rb-4.1.0&q=85&w=400"
                alt="Pizoo User 2"
                className="rounded-2xl shadow-2xl w-full h-64 object-cover mt-8"
                loading="lazy"
              />
              <img
                src="https://images.unsplash.com/photo-1606841216827-d1217fa5fe27?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwzfHx5b3VuZyUyMGFkdWx0JTIwcG9ydHJhaXR8ZW58MHx8fHwxNzY0OTI1ODc4fDA&ixlib=rb-4.1.0&q=85&w=400"
                alt="Pizoo User 3"
                className="rounded-2xl shadow-2xl w-full h-64 object-cover"
                loading="lazy"
              />
              <img
                src="https://images.unsplash.com/photo-1535295972055-1c762f4483e5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzR8MHwxfHNlYXJjaHwxfHxzbWlsaW5nJTIwcGVyc29ufGVufDB8fHx8MTc2NDkyNTg4N3ww&ixlib=rb-4.1.0&q=85&w=400"
                alt="Pizoo User 4"
                className="rounded-2xl shadow-2xl w-full h-64 object-cover mt-8"
                loading="lazy"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;