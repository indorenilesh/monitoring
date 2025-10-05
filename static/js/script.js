// JavaScript for interactive functionality
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle functionality
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
        
        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', function(event) {
            if (window.innerWidth <= 768) {
                if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }
    
    // Active menu item functionality
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all nav items
            navLinks.forEach(l => l.parentElement.classList.remove('active'));
            
            // Add active class to clicked nav item
            this.parentElement.classList.add('active');
        });
    });
    
    // Chart controls functionality
    const chartControls = document.querySelectorAll('.chart-controls .btn-secondary');
    
    chartControls.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons in the same control group
            const parentControls = this.parentElement;
            parentControls.querySelectorAll('.btn-secondary').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Add active class to clicked button
            this.classList.add('active');
        });
    });
    
    // Notification badge click functionality
    const notificationBtn = document.querySelector('.notification-btn');
    
    if (notificationBtn) {
        notificationBtn.addEventListener('click', function() {
            // Here you could show a notification dropdown
            console.log('Notifications clicked');
        });
    }
    
    // Search functionality
    const searchInput = document.querySelector('.search-box input');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            console.log('Searching for:', searchTerm);
            // Here you could implement actual search functionality
        });
    }
    
    // Add hover effects to stat cards
    const statCards = document.querySelectorAll('.stat-card');
    
    statCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Simulate real-time data updates
    function updateStats() {
        const statNumbers = document.querySelectorAll('.stat-info h3');
        
        statNumbers.forEach(stat => {
            const currentValue = stat.textContent;
            const numericValue = parseFloat(currentValue.replace(/[^0-9.]/g, ''));
            
            if (!isNaN(numericValue)) {
                // Add small random variation to simulate real-time updates
                const variation = (Math.random() - 0.5) * 0.02; // ±1% variation
                const newValue = numericValue * (1 + variation);
                
                if (currentValue.includes('$')) {
                    stat.textContent = '$' + Math.round(newValue).toLocaleString();
                } else if (currentValue.includes('%')) {
                    stat.textContent = newValue.toFixed(1) + '%';
                } else {
                    stat.textContent = Math.round(newValue).toLocaleString();
                }
            }
        });
    }
    
    // Update stats every 30 seconds
    setInterval(updateStats, 30000);
    
    // Add loading animation to chart placeholders
    const chartPlaceholders = document.querySelectorAll('.chart-placeholder');
    
    chartPlaceholders.forEach(placeholder => {
        const icon = placeholder.querySelector('i');
        
        if (icon) {
            setInterval(() => {
                icon.style.transform = 'rotate(360deg)';
                setTimeout(() => {
                    icon.style.transform = 'rotate(0deg)';
                }, 1000);
            }, 5000);
        }
    });
    
    // Keyboard shortcuts
    document.addEventListener('keydown', function(event) {
        // Ctrl/Cmd + K to focus search
        if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
            event.preventDefault();
            if (searchInput) {
                searchInput.focus();
            }
        }
        
        // Escape to close mobile sidebar
        if (event.key === 'Escape' && window.innerWidth <= 768) {
            sidebar.classList.remove('open');
        }
    });
    
    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('open');
        }
    });
    
    // Add smooth scrolling for better UX
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Initialize tooltips (if you want to add tooltips later)
    function initTooltips() {
        const elementsWithTooltips = document.querySelectorAll('[data-tooltip]');
        
        elementsWithTooltips.forEach(element => {
            element.addEventListener('mouseenter', function() {
                const tooltip = document.createElement('div');
                tooltip.className = 'tooltip';
                tooltip.textContent = this.getAttribute('data-tooltip');
                tooltip.style.cssText = `
                    position: absolute;
                    background: #333;
                    color: white;
                    padding: 0.5rem;
                    border-radius: 4px;
                    font-size: 0.8rem;
                    z-index: 1000;
                    pointer-events: none;
                `;
                
                document.body.appendChild(tooltip);
                
                const rect = this.getBoundingClientRect();
                tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
                tooltip.style.top = rect.top - tooltip.offsetHeight - 5 + 'px';
            });
            
            element.addEventListener('mouseleave', function() {
                const tooltip = document.querySelector('.tooltip');
                if (tooltip) {
                    tooltip.remove();
                }
            });
        });
    }
    
    // Initialize tooltips
    initTooltips();
    
    console.log('Dashboard initialized successfully!');
});
