#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
DEF_COLOR='\033[0;39m'

echo -e "${YELLOW}🔍 Running lint-strict...${DEF_COLOR}"

# Ejecutar make lint-strict
if ! make lint-strict; then
    echo -e "${RED}❌ Lint failed! Commit blocked.${DEF_COLOR}"
    exit 1
fi

echo -e "${GREEN}✅ Lint passed!${DEF_COLOR}"
echo ""
echo -e "${YELLOW}🔨 Building with uv build...${DEF_COLOR}"

# Ejecutar uv build
if ! uv build; then
    echo -e "${RED}❌ Build failed! Commit blocked.${DEF_COLOR}"
    exit 1
fi

echo -e "${GREEN}✅ Build successful!${DEF_COLOR}"
echo -e "${GREEN}✅ All checks passed! Commit allowed.${DEF_COLOR}"
exit 0
