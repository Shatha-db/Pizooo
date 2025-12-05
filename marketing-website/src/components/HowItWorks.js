import React from 'react';
import { useTranslation } from 'react-i18next';
import { UserPlus, Search, MessageSquare, Coffee } from 'lucide-react';

const HowItWorks = () => {
  const { t } = useTranslation();
  const icons = [UserPlus, Search, MessageSquare, Coffee];

  return (
    <section id="how-it-works" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16 animate-fade-in">
          <h2 className="text-4xl md:text-5xl font-bold mb-4 gradient-text">
            {t('howItWorks.title')}
          </h2>
          <p className="text-xl text-gray-600">
            {t('howItWorks.subtitle')}
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {t('howItWorks.steps', { returnObjects: true }).map((step, index) => {
            const Icon = icons[index];
            return (
              <div key={index} className="text-center animate-slide-up" style={{ animationDelay: `${index * 0.1}s` }}>
                <div className="relative mb-6">
                  <div className="w-20 h-20 gradient-bg rounded-full flex items-center justify-center mx-auto shadow-lg">
                    <Icon className="w-10 h-10 text-white" />
                  </div>
                  <div className="absolute -top-2 -right-2 w-8 h-8 bg-primary-500 rounded-full flex items-center justify-center text-white font-bold shadow-lg">
                    {index + 1}
                  </div>
                </div>
                <h3 className="text-2xl font-bold mb-3 text-gray-900">{step.title}</h3>
                <p className="text-gray-600 leading-relaxed">{step.description}</p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;