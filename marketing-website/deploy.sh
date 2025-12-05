#!/bin/bash

# Pizoo Marketing Website - Deployment Script
# Verwendung: ./deploy.sh [production|preview]

set -e  # Exit on error

echo "🚀 Pizoo Marketing Website Deployment"
echo "======================================"

# Farben für Output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Deployment Mode
MODE=${1:-preview}

if [ "$MODE" != "production" ] && [ "$MODE" != "preview" ]; then
    echo -e "${RED}❌ Ungültiger Modus. Verwenden Sie: production oder preview${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Deployment Modus: $MODE${NC}"
echo ""

# Schritt 1: Abhängigkeiten prüfen
echo "🔍 Schritt 1: Prüfe Abhängigkeiten..."
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js ist nicht installiert${NC}"
    exit 1
fi

if ! command -v yarn &> /dev/null; then
    echo -e "${RED}❌ Yarn ist nicht installiert${NC}"
    echo "Installieren Sie mit: npm install -g yarn"
    exit 1
fi

if ! command -v vercel &> /dev/null; then
    echo -e "${YELLOW}⚠️  Vercel CLI ist nicht installiert${NC}"
    echo "Installiere Vercel CLI..."
    npm install -g vercel
fi

echo -e "${GREEN}✅ Alle Abhängigkeiten vorhanden${NC}"
echo ""

# Schritt 2: Dependencies installieren
echo "📦 Schritt 2: Installiere Dependencies..."
yarn install
echo -e "${GREEN}✅ Dependencies installiert${NC}"
echo ""

# Schritt 3: Build erstellen
echo "🔨 Schritt 3: Erstelle Production Build..."
yarn build

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Build fehlgeschlagen${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Build erfolgreich${NC}"
echo ""

# Schritt 4: Build-Größe prüfen
echo "📊 Schritt 4: Build-Statistiken..."
BUILD_SIZE=$(du -sh build | cut -f1)
echo "Build-Größe: $BUILD_SIZE"
echo ""

# Schritt 5: Vercel Login prüfen
echo "🔐 Schritt 5: Vercel Login prüfen..."
vercel whoami &> /dev/null

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}⚠️  Nicht eingeloggt. Bitte einloggen:${NC}"
    vercel login
fi

echo -e "${GREEN}✅ Vercel Login aktiv${NC}"
echo ""

# Schritt 6: Deploy
echo "🚀 Schritt 6: Deploy zu Vercel..."

if [ "$MODE" = "production" ]; then
    echo -e "${YELLOW}🔥 Production Deployment startet...${NC}"
    vercel --prod --yes
else
    echo -e "${YELLOW}👀 Preview Deployment startet...${NC}"
    vercel --yes
fi

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Deployment erfolgreich!${NC}"
    echo ""
    
    if [ "$MODE" = "production" ]; then
        echo "🎉 Production URL: https://pizoo.ch"
    else
        echo "👀 Preview URL: (siehe oben)"
    fi
    
    echo ""
    echo "📋 Nächste Schritte:"
    if [ "$MODE" = "preview" ]; then
        echo "  1. Testen Sie die Preview URL"
        echo "  2. Wenn alles funktioniert: ./deploy.sh production"
    else
        echo "  1. Testen Sie https://pizoo.ch"
        echo "  2. Prüfen Sie alle Sprachen"
        echo "  3. Testen Sie auf Mobile"
    fi
else
    echo -e "${RED}❌ Deployment fehlgeschlagen${NC}"
    exit 1
fi
