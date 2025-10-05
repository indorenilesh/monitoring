# CSS Customization Guide for Django Monitoring System

## Overview
This guide explains different ways to customize CSS in your Django monitoring system.

## Method 1: External CSS Files (Recommended)

### Structure
```
static/
├── css/
│   ├── custom.css      # Main custom styles
│   ├── dashboard.css    # Dashboard-specific styles
│   └── components.css   # Component-specific styles
```

### Usage in Templates
```html
{% load static %}
<link href="{% static 'css/custom.css' %}" rel="stylesheet">
<link href="{% static 'css/dashboard.css' %}" rel="stylesheet">
```

### Benefits
- ✅ Organized and maintainable
- ✅ Reusable across templates
- ✅ Easy to version control
- ✅ Can be cached by browsers
- ✅ Supports CSS preprocessing (SASS/SCSS)

## Method 2: Inline Styles in Templates

### Usage
```html
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
    Content here
</div>
```

### When to Use
- Quick prototyping
- One-off styling
- Dynamic styles from backend

### Drawbacks
- ❌ Not reusable
- ❌ Hard to maintain
- ❌ Mixes presentation with content

## Method 3: Template-Level Style Blocks

### Usage
```html
{% block extra_css %}
<style>
    .custom-class {
        background: #f0f0f0;
        padding: 20px;
    }
</style>
{% endblock %}
```

### Benefits
- ✅ Template-specific styles
- ✅ Easy to override in child templates
- ✅ Organized within template structure

## Method 4: Django Static Files with CSS Variables

### CSS Variables Approach
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
}

.custom-button {
    background: var(--primary-color);
    color: white;
}
```

### Dynamic CSS Generation
```python
# In views.py
def dynamic_css(request):
    theme = request.GET.get('theme', 'default')
    css_content = f"""
    :root {{
        --primary-color: {get_theme_color(theme)};
    }}
    """
    return HttpResponse(css_content, content_type='text/css')
```

## Method 5: CSS Framework Customization

### Bootstrap Customization
```css
/* Override Bootstrap variables */
:root {
    --bs-primary: #667eea;
    --bs-secondary: #764ba2;
}

/* Custom Bootstrap components */
.btn-custom {
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 600;
}
```

### Tailwind CSS Integration
```html
<!-- Add Tailwind CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    primary: '#667eea',
                    secondary: '#764ba2'
                }
            }
        }
    }
</script>
```

## Method 6: CSS Preprocessing (SASS/SCSS)

### Setup with Django
1. Install django-sass-processor:
```bash
pip install django-sass-processor
```

2. Add to settings.py:
```python
INSTALLED_APPS = [
    'sass_processor',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]
```

3. Create SCSS files:
```scss
// static/scss/main.scss
$primary-color: #667eea;
$secondary-color: #764ba2;

.custom-hero {
    background: linear-gradient(135deg, $primary-color 0%, $secondary-color 100%);
    
    .container {
        position: relative;
        z-index: 2;
    }
}
```

## Method 7: Component-Based CSS Architecture

### BEM Methodology
```css
/* Block */
.card { }

/* Element */
.card__header { }
.card__body { }
.card__footer { }

/* Modifier */
.card--featured { }
.card--warning { }
```

### CSS Modules Approach
```css
/* components/Button.module.css */
.button {
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
}

.primary {
    background-color: #667eea;
    color: white;
}

.secondary {
    background-color: #6c757d;
    color: white;
}
```

## Method 8: Responsive Design Patterns

### Mobile-First Approach
```css
/* Base styles for mobile */
.custom-card {
    padding: 1rem;
    margin: 0.5rem;
}

/* Tablet and up */
@media (min-width: 768px) {
    .custom-card {
        padding: 2rem;
        margin: 1rem;
    }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .custom-card {
        padding: 3rem;
        margin: 2rem;
    }
}
```

### Container Queries (Modern CSS)
```css
@container (min-width: 300px) {
    .card-content {
        display: flex;
        flex-direction: row;
    }
}
```

## Method 9: CSS-in-JS Integration

### For React Components (if using Django + React)
```javascript
const styles = {
    hero: {
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        padding: '100px 0',
        color: 'white'
    }
};

const Hero = () => (
    <section style={styles.hero}>
        <div className="container">
            <h1>Monitoring System</h1>
        </div>
    </section>
);
```

## Method 10: CSS Custom Properties for Theming

### Light/Dark Theme Support
```css
:root {
    --bg-color: #ffffff;
    --text-color: #333333;
    --card-bg: #f8f9fa;
}

[data-theme="dark"] {
    --bg-color: #1a1a1a;
    --text-color: #ffffff;
    --card-bg: #2d2d2d;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
}

.custom-card {
    background-color: var(--card-bg);
}
```

### JavaScript Theme Toggle
```javascript
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}
```

## Best Practices

### 1. Organization
- Use consistent naming conventions
- Group related styles together
- Comment complex CSS rules
- Use CSS custom properties for consistency

### 2. Performance
- Minify CSS in production
- Use CSS purging to remove unused styles
- Leverage browser caching
- Avoid deep nesting in CSS

### 3. Maintainability
- Use CSS methodologies (BEM, OOCSS)
- Keep specificity low
- Use semantic class names
- Document complex animations

### 4. Accessibility
- Ensure sufficient color contrast
- Use relative units for responsive design
- Test with screen readers
- Provide focus indicators

## Tools and Resources

### CSS Frameworks
- Bootstrap 5
- Tailwind CSS
- Bulma
- Foundation

### CSS Preprocessors
- Sass/SCSS
- Less
- Stylus

### Build Tools
- Webpack
- Vite
- Parcel
- Gulp

### CSS Utilities
- PostCSS
- Autoprefixer
- CSSnano
- PurgeCSS

## Example: Complete Custom Theme

```css
/* static/css/theme.css */
:root {
    /* Color Palette */
    --primary: #667eea;
    --primary-dark: #5a6fd8;
    --secondary: #764ba2;
    --success: #28a745;
    --warning: #ffc107;
    --danger: #dc3545;
    --info: #17a2b8;
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-size-base: 16px;
    --line-height-base: 1.5;
    
    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 3rem;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
    
    /* Border Radius */
    --radius-sm: 0.25rem;
    --radius-md: 0.5rem;
    --radius-lg: 1rem;
    --radius-xl: 1.5rem;
}

/* Base Styles */
body {
    font-family: var(--font-family);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
}

/* Component Styles */
.btn-primary {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    border: none;
    border-radius: var(--radius-md);
    padding: var(--spacing-sm) var(--spacing-lg);
    color: white;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.card {
    background: white;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    padding: var(--spacing-lg);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}
```

This comprehensive guide covers all the major approaches to CSS customization in Django. Choose the method that best fits your project's needs and team preferences!


