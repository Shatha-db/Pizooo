# Pizoo Marketing Website

## Overview
This is the official marketing website for Pizoo Dating App. Built with React, Tailwind CSS, and i18next for multi-language support.

## Features
- 🌍 **Multi-language Support**: 10+ languages (English, Arabic, German, French, Spanish, Italian, Portuguese, Russian, Chinese, Japanese)
- 🎨 **Modern Design**: Beautiful gradient colors and animations
- 📱 **Responsive**: Works perfectly on all devices
- 📝 **Blog CMS**: Built-in content management system for blog posts
- 🚀 **Fast**: Optimized for performance
- ♿ **Accessible**: Built with accessibility in mind

## Installation

```bash
# Install dependencies
yarn install

# Start development server
yarn start

# Build for production
yarn build
```

## Directory Structure

```
marketing-website/
├── public/
│   ├── index.html
│   └── manifest.json
├── src/
│   ├── components/      # Reusable components
│   │   ├── Header.js
│   │   ├── Hero.js
│   │   ├── Features.js
│   │   ├── HowItWorks.js
│   │   ├── SuccessStories.js
│   │   ├── Statistics.js
│   │   ├── Blog.js
│   │   ├── Download.js
│   │   └── Footer.js
│   ├── pages/          # Page components
│   │   ├── BlogPage.js
│   │   └── AdminBlog.js
│   ├── i18n/           # Internationalization
│   │   ├── i18n.js
│   │   └── locales/    # Translation files
│   ├── App.js
│   └── index.js
├── package.json
├── tailwind.config.js
└── README.md
```

## Pages

### Home Page
- Hero Section with Call-to-Action
- Features showcase
- How It Works section
- Success Stories
- Statistics
- Blog preview
- Download links

### Blog Page (`/blog`)
- Lists all blog articles
- Filter by category
- Search functionality

### Admin Panel (`/admin/blog`)
- Create new articles
- Edit existing articles
- Delete articles
- Manage blog content

## Language Support

The website automatically detects the user's browser language and displays content in that language. Users can also manually switch languages using the language selector in the header.

Supported languages:
- English (en)
- Arabic (ar)
- German (de)
- French (fr)
- Spanish (es)
- Italian (it)
- Portuguese (pt)
- Russian (ru)
- Chinese (zh)
- Japanese (ja)

## Blog CMS

The built-in CMS allows you to:
1. Create new blog posts
2. Edit existing posts
3. Delete posts
4. Add images, categories, and authors

Access the CMS at: `/admin/blog`

All blog data is stored in localStorage for simplicity. For production, you should integrate with a backend API.

## Deployment

### Deploy to pizoo.ch

1. Build the production version:
```bash
yarn build
```

2. The `build` folder contains the static files ready for deployment.

3. Configure your web server to:
   - Serve the `build` folder
   - Route all requests to `index.html` (for client-side routing)

### Integration with Main App

The marketing website is designed to work alongside the main Pizoo app. All "Sign In" and "Get Started" buttons open the main app at:
```
https://pizoo-debug.preview.emergentagent.com
```

Update this URL in the following components when deploying to production:
- `src/components/Header.js`
- `src/components/Hero.js`
- `src/components/Download.js`

## Customization

### Colors
Edit `tailwind.config.js` to change the color scheme:
```javascript
colors: {
  primary: { ... },  // Pink colors
  secondary: { ... }, // Purple colors
}
```

### Content
Update translation files in `src/i18n/locales/` to change website content.

### Images
Replace the Unsplash image URLs with your own images.

## Support

For questions or issues, contact the Pizoo development team.
