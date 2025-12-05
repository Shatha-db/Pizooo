import React from 'react';
import { useTranslation } from 'react-i18next';

const Statistics = () => {
  const { t } = useTranslation();

  return (
    <section className="py-20 gradient-bg text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16 animate-fade-in">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            {t('statistics.title')}
          </h2>
          <p className="text-xl text-white/90">
            {t('statistics.subtitle')}
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {t('statistics.items', { returnObjects: true }).map((stat, index) => (
            <div
              key={index}
              className="text-center p-8 bg-white/10 backdrop-blur-sm rounded-2xl hover:bg-white/20 transition animate-slide-up"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <h3 className="text-5xl font-bold mb-2">{stat.value}</h3>
              <p className="text-xl text-white/90">{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Statistics;