import React from 'react';
import { useTranslation } from 'react-i18next';
import { Facebook, Twitter, Instagram, Linkedin, Youtube, Heart } from 'lucide-react';

const Footer = () => {
  const { t } = useTranslation();

  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid md:grid-cols-4 gap-8 mb-12">
          {/* Logo & Description */}
          <div className="md:col-span-1">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-10 h-10 gradient-bg rounded-full flex items-center justify-center">
                <span className="text-white font-bold text-xl">P</span>
              </div>
              <span className="text-2xl font-bold">Pizoo</span>
            </div>
            <p className="text-gray-400 mb-6">
              {t('footer.description')}
            </p>
            <div className="flex space-x-4">
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-primary-500 transition">
                <Facebook className="w-5 h-5" />
              </a>
              <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-primary-500 transition">
                <Twitter className="w-5 h-5" />
              </a>
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-primary-500 transition">
                <Instagram className="w-5 h-5" />
              </a>
              <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-primary-500 transition">
                <Linkedin className="w-5 h-5" />
              </a>
              <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-primary-500 transition">
                <Youtube className="w-5 h-5" />
              </a>
            </div>
          </div>

          {/* Company Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">{t('footer.company.title')}</h3>
            <ul className="space-y-3">
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.company.about')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.company.careers')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.company.press')}</a></li>
              <li><a href="/blog" className="text-gray-400 hover:text-primary-500 transition">{t('footer.company.blog')}</a></li>
            </ul>
          </div>

          {/* Support Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">{t('footer.support.title')}</h3>
            <ul className="space-y-3">
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.support.help')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.support.safety')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.support.contact')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.support.faq')}</a></li>
            </ul>
          </div>

          {/* Legal Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">{t('footer.legal.title')}</h3>
            <ul className="space-y-3">
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.legal.terms')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.legal.privacy')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.legal.cookies')}</a></li>
              <li><a href="#" className="text-gray-400 hover:text-primary-500 transition">{t('footer.legal.community')}</a></li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-400 text-sm mb-4 md:mb-0">
            {t('footer.copyright')}
          </p>
          <p className="text-gray-400 text-sm flex items-center">
            Made with <Heart className="w-4 h-4 mx-1 text-primary-500 fill-current" /> by Pizoo Team
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;