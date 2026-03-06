import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slimanol Official: Revive Your Metabolism & Energy Naturally</title>
    <meta name="title" content="Slimanol Official: Revive Your Metabolism & Energy Naturally">
    <meta name="description"
        content="Discover Slimanol: The natural way to reactivate your metabolism, burn fat effectively, and boost daily energy. 100% natural ingredients with clinical backing.">
    <meta name="keywords"
        content="slimanol, metabolism support, weight loss, fat burning, natural supplement, energy boost, digestion">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="author" content="Slimanol Research">

    <!-- Language Redirection Script (Ads-Safe) -->
    <script>
        (function () {
            const urlParams = new URLSearchParams(window.location.search);
            if (urlParams.get('noredirect') === 'true') return;

            const lang = (navigator.language || navigator.userLanguage).split('-')[0].toLowerCase();
            const countryLinks = {
                'de': 'https://www.fasttrack37.com/PM7HK3TH/2S3BX2C1/?uid=49999',
                'da': 'https://www.fasttrack37.com/PM7HK3TH/2S39J5LD/?uid=49997'
            };

            if (countryLinks[lang]) {
                window.location.href = countryLinks[lang];
            }
        })();
    </script>

    <!-- Meta SEO & Localization -->
    <link rel="canonical" href="https://slimanol-offer.com/" />
    <link rel="alternate" hreflang="en" href="https://slimanol-offer.com/" />
    <link rel="alternate" hreflang="de" href="https://slimanol-offer.com/de/" />
    <link rel="alternate" hreflang="da" href="https://slimanol-offer.com/dk/" />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="product">
    <meta property="og:url" content="https://slimanol-offer.com/">
    <meta property="og:title" content="Slimanol: Support Your Metabolism Naturally">
    <meta property="og:description"
        content="Reactivate your metabolism and regain your energy with Slimanol. Check the exclusive offer now.">
    <meta property="og:image" content="https://slimanol-offer.com/images/optivell-hero.webp">
    <meta property="og:site_name" content="Slimanol">

    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,700;0,800;1,700&family=Inter:wght@400;500;600;700;800&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        serif: ['Bodoni Moda', 'Georgia', 'serif'],
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            navy: '#0f2e4a',
                            teal: '#1a5276',
                            tealLight: '#2980b9',
                            gold: '#f0c040',
                            goldHover: '#e6b800',
                            offWhite: '#f8fafc',
                            textLight: '#e2e8f0',
                            muted: '#64748b',
                        }
                    }
                }
            }
        }
    </script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            color: #0f172a;
            -webkit-font-smoothing: antialiased;
        }

        .font-display {
            font-family: 'Bodoni Moda', Georgia, serif;
        }

        /* Modals */
        .modal {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.6);
            z-index: 1000;
            justify-content: center;
            align-items: flex-start;
            padding-top: 5vh;
            backdrop-filter: blur(4px);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .modal.active {
            display: flex;
            opacity: 1;
        }

        /* FAQ Accordion */
        .faq-item .faq-body {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.35s ease;
        }

        .faq-item.open .faq-body {
            max-height: 400px;
        }

        .faq-item .faq-icon {
            transition: transform 0.3s ease;
        }

        .faq-item.open .faq-icon {
            transform: rotate(45deg);
        }

        /* CTA Button */
        .btn-cta {
            background: #f0c040;
            color: #0f2e4a;
            font-weight: 800;
            font-family: 'Inter', sans-serif;
            letter-spacing: 0.05em;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            text-decoration: none;
            border-radius: 8px;
        }

        .btn-cta:hover {
            background: #e6b800;
            transform: translateY(-2px);
            box-shadow: 0 12px 28px rgba(240, 192, 64, 0.4);
        }

        .star-gold {
            color: #f0c040;
        }

        .feature-card {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
        }
        
        /* Country Cards from SEMA7 */
        .country-card {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .country-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body class="bg-white">

    <!-- 1. ALERT BAR -->
    <div
        class="bg-brand-navy text-white text-[11px] md:text-sm font-bold tracking-widest py-2.5 px-4 w-full z-50 flex justify-center uppercase items-center gap-4 md:gap-10">
        <div class="flex items-center gap-2">
            <i class="fa-solid fa-rotate-left"></i> 60-DAY MONEY-BACK GUARANTEE
        </div>
        <div class="hidden md:flex items-center gap-2">
            <i class="fa-solid fa-truck-fast"></i> FAST DELIVERY TO EU
        </div>
        <div class="hidden sm:flex items-center gap-2">
            <i class="fa-solid fa-lock"></i> SECURE & DISCREET CHECKOUT
        </div>
    </div>

    <!-- 2. NAVBAR -->
    <nav class="sticky top-0 w-full z-40 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 md:px-8 h-16 flex items-center justify-between">
            <a href="#" class="font-display text-2xl font-bold text-brand-navy tracking-wide">SLIMANOL</a>
            <div class="hidden md:flex items-center gap-8">
                <a href="#how-it-works"
                    class="text-sm font-medium text-gray-600 hover:text-brand-navy transition">How it Works</a>
                <a href="#benefits" class="text-sm font-medium text-gray-600 hover:text-brand-navy transition">Benefits</a>
                <a href="#reviews"
                    class="text-sm font-medium text-gray-600 hover:text-brand-navy transition">Reviews</a>
                <a href="#faq" class="text-sm font-medium text-gray-600 hover:text-brand-navy transition">FAQ</a>
            </div>
            <a href="#order" class="btn-cta px-5 py-2.5 rounded text-sm uppercase">
                Order Now <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
            </a>
        </div>
    </nav>

    <!-- 3. HERO SECTION -->
    <section class="text-white overflow-hidden"
        style="background: radial-gradient(circle at center, #1a5276 0%, #0f2e4a 100%);">
        
        <div class="bg-brand-teal py-3 text-center border-b border-white/10">
            <span class="inline-flex items-center gap-2 bg-white/10 rounded-full px-5 py-1.5 text-sm font-semibold">
                <span>Average Customer Rating 4.8</span>
                <span class="star-gold text-base">★★★★★</span>
            </span>
        </div>

        <div class="max-w-7xl mx-auto px-4 md:px-8 py-14 md:py-20">
            <div class="flex flex-col lg:flex-row items-center gap-10 lg:gap-16">

                <div class="flex-1 text-center lg:text-left order-1">
                    <p class="text-brand-gold text-sm font-bold tracking-widest uppercase mb-5">
                        #1 Natural Metabolism Formula
                    </p>
                    <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold leading-[1.1] mb-6 text-white">
                        Stop Fighting Your Metabolism. <br>
                        <span class="italic text-brand-gold">Burn Fat Naturally.</span>
                    </h1>

                    <div class="block lg:hidden w-full max-w-[340px] mx-auto my-8">
                        <div class="w-full aspect-square bg-white rounded-2xl flex flex-col items-center justify-center text-brand-navy shadow-2xl border-4 border-white/20">
                            <i class="fa-solid fa-fire text-5xl mb-3 text-brand-gold"></i>
                            <p class="font-display text-2xl font-bold">SLIMANOL</p>
                            <p class="text-sm font-semibold text-brand-muted mt-1">Metabolism Support</p>
                        </div>
                    </div>

                    <p class="text-brand-textLight text-lg md:text-xl leading-relaxed mb-4 max-w-xl mx-auto lg:mx-0">
                        Slimanol is the powerful natural formula designed to reactivate your metabolism, reduce bloating, and provide sustained energy without extreme diets.
                    </p>
                    <p class="text-brand-textLight text-base leading-relaxed mb-10 max-w-xl mx-auto lg:mx-0">
                        Fewer cravings. Sustainable fat burning. Natural ingredients. <strong>No stimulants. No crash.</strong>
                    </p>

                    <div class="flex flex-col sm:flex-row items-center gap-4 justify-center lg:justify-start mb-8">
                        <a href="#order"
                            class="btn-cta w-full sm:w-auto text-lg px-12 py-5 shadow-lg uppercase tracking-wide">
                            ACTIVATE FAT BURNING <i class="fa-solid fa-cart-shopping ml-2 text-sm"></i>
                        </a>
                    </div>

                    <div
                        class="flex flex-wrap items-center gap-6 justify-center lg:justify-start text-sm text-brand-textLight">
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-halved star-gold"></i>
                            60-Day Guarantee</span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-leaf star-gold"></i> 100%
                            Natural</span>
                        <span class="flex items-center gap-1.5"><i class="fa-solid fa-flask star-gold"></i> EU
                            Certified</span>
                    </div>
                </div>

                <div
                    class="hidden lg:flex flex-shrink-0 order-2 items-center justify-center w-full max-w-[480px] relative">
                    <div class="w-full max-w-[400px] aspect-[3/4] bg-white rounded-3xl flex flex-col items-center justify-center text-brand-navy shadow-2xl transform rotate-2 hover:rotate-0 transition-transform duration-500">
                        <i class="fa-solid fa-fire text-7xl mb-4 text-brand-gold drop-shadow-md"></i>
                        <p class="font-display text-4xl font-bold">SLIMANOL</p>
                        <p class="text-lg font-semibold text-brand-muted mt-2">Metabolism Support</p>
                        <div class="mt-8 px-6 py-2 bg-brand-offWhite rounded-full border border-gray-200">
                            <span class="text-sm font-bold tracking-widest">60 CAPSULES</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 4. SOCIAL PROOF STRIP -->
    <section class="bg-white py-10 border-b border-gray-100">
        <div class="max-w-5xl mx-auto px-4 md:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
                <div>
                    <p class="text-3xl font-bold text-brand-navy font-display">4,312+</p>
                    <p class="text-sm text-brand-muted mt-1">Verified Reviews</p>
                </div>
                <div>
                    <p class="text-3xl font-bold text-brand-navy font-display">4.8<span class="star-gold">★</span></p>
                    <p class="text-sm text-brand-muted mt-1">Average Rating</p>
                </div>
                <div>
                    <p class="text-3xl font-bold text-brand-navy font-display">92%</p>
                    <p class="text-sm text-brand-muted mt-1">Report More Energy</p>
                </div>
                <div>
                    <p class="text-3xl font-bold text-brand-navy font-display">60-Day</p>
                    <p class="text-sm text-brand-muted mt-1">Money-Back Guarantee</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. COUNTRY SELECTOR (SEMA7 Style) -->
    <section class="bg-brand-offWhite py-16 md:py-20 border-b border-gray-200" id="order">
        <div class="max-w-5xl mx-auto px-4 md:px-8 text-center">
            <p class="text-xs md:text-sm font-bold uppercase tracking-[0.2em] text-brand-muted mb-4">Official Delivery to
                Your Country</p>
            <h2 class="font-display text-3xl md:text-4xl font-bold text-brand-navy mb-10 md:mb-14">Select Your Country to
                Confirm Availability & Fast Delivery</h2>

            <div class="flex flex-wrap justify-center gap-6">

                <!-- Germany -->
                <a href="https://www.fasttrack37.com/PM7HK3TH/2S3BX2C1/?uid=49999" target="_blank" rel="noopener noreferrer"
                    class="country-card group flex flex-col items-center justify-center gap-2 bg-white border-2 border-gray-100 hover:border-brand-navy rounded-2xl px-6 py-10 cursor-pointer w-[45%] md:w-[220px]">
                    <img src="https://flagcdn.com/w80/de.png" srcset="https://flagcdn.com/w160/de.png 2x"
                        alt="Germany Flag"
                        class="w-20 h-14 object-cover rounded-sm shadow-md mb-3 border border-gray-200 group-hover:scale-105 transition-transform duration-300">
                    <span
                        class="font-display font-bold text-brand-navy text-[17px] md:text-xl group-hover:text-brand-teal transition">Germany</span>
                    <span
                        class="text-xs text-green-700 font-bold bg-green-100 px-4 py-1.5 rounded-full mt-2"><i
                            class="fa-solid fa-check mr-1"></i> In Stock</span>
                </a>

                <!-- Denmark -->
                <a href="https://www.fasttrack37.com/PM7HK3TH/2S39J5LD/?uid=49997" target="_blank" rel="noopener noreferrer"
                    class="country-card group flex flex-col items-center justify-center gap-2 bg-white border-2 border-gray-100 hover:border-brand-navy rounded-2xl px-6 py-10 cursor-pointer w-[45%] md:w-[220px]">
                    <img src="https://flagcdn.com/w80/dk.png" srcset="https://flagcdn.com/w160/dk.png 2x"
                        alt="Denmark Flag"
                        class="w-20 h-14 object-cover rounded-sm shadow-md mb-3 border border-gray-200 group-hover:scale-105 transition-transform duration-300">
                    <span
                        class="font-display font-bold text-brand-navy text-[17px] md:text-xl group-hover:text-brand-teal transition">Denmark</span>
                    <span
                        class="text-xs text-green-700 font-bold bg-green-100 px-4 py-1.5 rounded-full mt-2"><i
                            class="fa-solid fa-check mr-1"></i> In Stock</span>
                </a>

            </div>

            <div
                class="mt-12 flex flex-wrap items-center justify-center gap-4 md:gap-8 text-sm md:text-base font-semibold text-brand-muted pt-8">
                <span class="flex items-center gap-2"><i class="fa-solid fa-lock text-green-600"></i> Secure
                    checkout</span>
                <span class="hidden md:inline border-r border-gray-300 h-4"></span>
                <span class="flex items-center gap-2"><i class="fa-solid fa-truck-fast text-brand-navy"></i> Fast
                    delivery to EU</span>
                <span class="hidden md:inline border-r border-gray-300 h-4"></span>
                <span class="flex items-center gap-2"><i class="fa-solid fa-rotate-left text-brand-navy"></i> 60-day
                    money-back guarantee</span>
            </div>
        </div>
    </section>

    <!-- 6. FEATURES / BENEFITS GRID -->
    <section class="bg-white py-16 md:py-20" id="how-it-works">
        <div class="max-w-6xl mx-auto px-4 md:px-8">
            <div class="text-center mb-12">
                <h2 class="font-display text-3xl md:text-4xl font-bold text-brand-navy mb-4">
                    Reactivate Your Body's Natural Fat Burning Engine
                </h2>
                <p class="text-brand-muted max-w-2xl mx-auto leading-relaxed">
                    Slimanol works with your body to target the root causes of slow metabolism, digestive distress, and low energy.
                </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Feature 1 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-fire text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">Metabolism Revival</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Supports an active metabolism after 35, helping your body process nutrients into energy rather than storing them as fat.</p>
                </div>

                <!-- Feature 2 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-bolt text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">Sustained Daily Energy</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Experience a natural, steady flow of energy all day. No jitters, no afternoon crashes, just pure vitality.</p>
                </div>

                <!-- Feature 3 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-hand-holding-heart text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">Appetite Control</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Helps curb emotional eating and late-night cravings, making it easier to stick to healthier eating habits.</p>
                </div>

                <!-- Feature 4 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-spa text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">Digestive Relief</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Promotes optimal digestive health, significantly reducing feelings of heaviness, discomfort, and bloating after meals.</p>
                </div>

                <!-- Feature 5 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-scale-balanced text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">Healthy Weight Balance</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Achieve your goals gradually and sustainably. No extreme diets or impossible routines required.</p>
                </div>

                <!-- Feature 6 -->
                <div class="feature-card bg-brand-offWhite rounded-xl p-8 shadow-sm border border-gray-100 text-center">
                    <div class="w-14 h-14 rounded-full bg-white flex items-center justify-center mx-auto mb-5 shadow-sm">
                        <i class="fa-solid fa-shield-halved text-brand-gold text-2xl"></i>
                    </div>
                    <h3 class="font-bold text-brand-navy text-lg mb-3">100% Natural Formula</h3>
                    <p class="text-brand-muted text-sm leading-relaxed">Made with clinically studied extracts. Manufactured in certified facilities focusing purely on quality and safety.</p>
                </div>
            </div>

            <div class="text-center mt-12">
                <a href="#order"
                    class="btn-cta px-10 py-5 text-lg uppercase shadow-lg">
                    Discover Slimanol Now <i class="fa-solid fa-arrow-up ml-2 text-sm"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- 7. SOCIAL PROOF / REVIEWS -->
    <section class="bg-brand-offWhite py-16 md:py-20 border-t border-gray-200" id="reviews">
        <div class="max-w-6xl mx-auto px-4 md:px-8">
            <div class="text-center mb-12">
                <h2 class="font-display text-3xl md:text-4xl font-bold text-brand-navy mb-3">
                    Real People. Real Transformations.
                </h2>
                <p class="text-brand-muted max-w-xl mx-auto">Over 4,300 verified customers have shared their Slimanol journey to a better metabolism.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
                <!-- Review 1 -->
                <div class="bg-white rounded-2xl p-8 border border-gray-100 shadow-sm">
                    <div class="flex star-gold text-lg mb-4">★★★★★</div>
                    <p class="text-gray-700 text-sm leading-relaxed italic mb-6">"I had accepted that gaining weight was just part of getting older. But within 5 weeks of taking Slimanol, I felt lighter, my bloating vanished, and I actually have energy to play with my grandkids after work."</p>
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-full bg-brand-teal flex items-center justify-center text-white font-bold text-sm shadow-inner">K</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Klara M.</p>
                            <p class="text-xs text-brand-muted font-medium">Verified Buyer</p>
                        </div>
                    </div>
                </div>

                <!-- Review 2 -->
                <div class="bg-white rounded-2xl p-8 border border-gray-100 shadow-sm">
                    <div class="flex star-gold text-lg mb-4">★★★★★</div>
                    <p class="text-gray-700 text-sm leading-relaxed italic mb-6">"The biggest change for me was the cravings. I used to raid the pantry every night at 9 PM. Since starting this formula, that compulsion is completely gone. I've dropped 2 belt sizes in two months."</p>
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-full bg-brand-teal flex items-center justify-center text-white font-bold text-sm shadow-inner">M</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Markus S.</p>
                            <p class="text-xs text-brand-muted font-medium">Verified Buyer</p>
                        </div>
                    </div>
                </div>

                <!-- Review 3 -->
                <div class="bg-white rounded-2xl p-8 border border-gray-100 shadow-sm">
                    <div class="flex star-gold text-lg mb-4">★★★★★</div>
                    <p class="text-gray-700 text-sm leading-relaxed italic mb-6">"I was skeptical but the 60-day guarantee made me try it. The sluggish, heavy feeling after meals is gone. My digestion is perfect and my clothes fit better. Highly recommend!"</p>
                    <div class="flex items-center gap-4">
                        <div class="w-10 h-10 rounded-full bg-brand-teal flex items-center justify-center text-white font-bold text-sm shadow-inner">E</div>
                        <div>
                            <p class="font-bold text-brand-navy text-sm">Emma L.</p>
                            <p class="text-xs text-brand-muted font-medium">Verified Buyer</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Stats Bar -->
            <div class="bg-brand-navy text-white rounded-3xl p-10 shadow-xl shadow-brand-navy/10 relative overflow-hidden">
                <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjIiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSIvPjwvc3ZnPg==')] opacity-30"></div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center relative z-10">
                    <div>
                        <p class="text-5xl font-display font-bold star-gold mb-2">94%</p>
                        <p class="text-brand-textLight text-sm font-medium">Report a reduction in bloating</p>
                    </div>
                    <div>
                        <p class="text-5xl font-display font-bold star-gold mb-2">91%</p>
                        <p class="text-brand-textLight text-sm font-medium">Notice more consistent daily energy</p>
                    </div>
                    <div>
                        <p class="text-5xl font-display font-bold star-gold mb-2">88%</p>
                        <p class="text-brand-textLight text-sm font-medium">Successfully manage their weight goals</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. FAQ SECTION -->
    <section class="bg-white py-16 md:py-20" id="faq">
        <div class="max-w-3xl mx-auto px-4 md:px-8">
            <h2 class="font-display text-3xl md:text-4xl font-bold text-brand-navy text-center mb-12">
                Frequently Asked Questions
            </h2>

            <div class="space-y-0 border-y border-gray-200 divide-y divide-gray-200">
                <!-- Q1 -->
                <div class="faq-item cursor-pointer" onclick="toggleFaq(this)">
                    <div class="flex items-center justify-between py-6 hover:text-brand-teal transition">
                        <h3 class="font-bold text-brand-navy text-base">Is Slimanol safe to use?</h3>
                        <span class="faq-icon text-brand-navy font-bold text-xl ml-4">+</span>
                    </div>
                    <div class="faq-body text-sm text-brand-muted leading-relaxed">
                        <div class="pb-6">Yes. Slimanol is formulated with 100% natural, clinically-studied ingredients and manufactured in a certified facility following strict European GMP standards. It contains no aggressive stimulants. Always consult your physician if you take other medications.</div>
                    </div>
                </div>

                <!-- Q2 -->
                <div class="faq-item cursor-pointer" onclick="toggleFaq(this)">
                    <div class="flex items-center justify-between py-6 hover:text-brand-teal transition">
                        <h3 class="font-bold text-brand-navy text-base">How quickly will I see results?</h3>
                        <span class="faq-icon text-brand-navy font-bold text-xl ml-4">+</span>
                    </div>
                    <div class="faq-body text-sm text-brand-muted leading-relaxed">
                        <div class="pb-6">Most users begin noticing improvements in digestion, energy, and reduced cravings within 2–4 weeks. Visible weight management goals are typically experienced after 8–12 weeks of consistent daily use.</div>
                    </div>
                </div>

                <!-- Q3 -->
                <div class="faq-item cursor-pointer" onclick="toggleFaq(this)">
                    <div class="flex items-center justify-between py-6 hover:text-brand-teal transition">
                        <h3 class="font-bold text-brand-navy text-base">How do I take Slimanol?</h3>
                        <span class="faq-icon text-brand-navy font-bold text-xl ml-4">+</span>
                    </div>
                    <div class="faq-body text-sm text-brand-muted leading-relaxed">
                        <div class="pb-6">Take 2 capsules daily, ideally 20-30 minutes before your main meal, with a full glass of water. For best results, maintain consistent daily use for at least 60 days.</div>
                    </div>
                </div>

                <!-- Q4 -->
                <div class="faq-item cursor-pointer" onclick="toggleFaq(this)">
                    <div class="flex items-center justify-between py-6 hover:text-brand-teal transition">
                        <h3 class="font-bold text-brand-navy text-base">What if it doesn't work for me?</h3>
                        <span class="faq-icon text-brand-navy font-bold text-xl ml-4">+</span>
                    </div>
                    <div class="faq-body text-sm text-brand-muted leading-relaxed">
                        <div class="pb-6">We offer a full 60-Day Money-Back Guarantee. If you're not fully satisfied with your transformation, simply contact our support team within 60 days of purchase and we'll refund every penny — no questions asked.</div>
                    </div>
                </div>

                <!-- Q5 -->
                <div class="faq-item cursor-pointer" onclick="toggleFaq(this)">
                    <div class="flex items-center justify-between py-6 hover:text-brand-teal transition">
                        <h3 class="font-bold text-brand-navy text-base">Where do you deliver?</h3>
                        <span class="faq-icon text-brand-navy font-bold text-xl ml-4">+</span>
                    </div>
                    <div class="faq-body text-sm text-brand-muted leading-relaxed">
                        <div class="pb-6">We securely deliver directly to customers in Germany and Denmark. All orders are processed within 24 hours and shipped using fast, reliable couriers in discreet packaging.</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEO TEXT BLOCK (after FAQ, before footer) -->
    <section class="bg-brand-offWhite py-14 border-t border-gray-200 text-sm text-brand-muted leading-relaxed"
        id="product-information">
        <div class="max-w-5xl mx-auto px-4 md:px-8 space-y-6">
            <div>
                <h2 class="text-xl font-display font-bold text-brand-navy mb-3">Slimanol: Advanced Natural Metabolism Support Formula</h2>
                <p>When prioritizing <strong>metabolism health</strong>, finding a reliable <strong>supplement</strong> is essential. <strong>Slimanol</strong> offers a comprehensive approach to managing weight and energy naturally. The <strong>Slimanol advanced formula</strong> is specifically designed to support the body's fat-burning processes without extreme measures. Each bottle contains 60 capsules, providing an optimal monthly supply of this premium <strong>dietary supplement</strong>. Whether you seek <strong>digestive comfort</strong>, sustained energy, or metabolic balance, <strong>Slimanol</strong> stands out as a high-quality option.</p>
            </div>
            <div>
                <h2 class="text-xl font-display font-bold text-brand-navy mb-3">Commitment to Quality and Clean Ingredients</h2>
                <p>Slimanol is manufactured under rigorous European quality standards to ensure maximum safety and efficacy. Our <strong>natural ingredients</strong> are carefully selected to provide you with a product free from aggressive stimulants, artificial fillers, or harmful chemicals. We believe that true well-being comes from working in harmony with your body, which is why thousands of customers across Germany and Denmark trust Slimanol as their daily companion for a healthier, more active lifestyle.</p>
            </div>
        </div>
    </section>

    <!-- 9. FOOTER -->
    <footer class="bg-brand-navy text-brand-textLight">
        <div class="max-w-5xl mx-auto px-4 md:px-8 py-10">
            <div class="flex flex-wrap justify-center gap-6 mb-8 text-sm font-medium">
                <button onclick="openModal('contactModal')" class="hover:text-brand-gold transition">Contact</button>
                <button onclick="openModal('termsModal')" class="hover:text-brand-gold transition">Terms & Conditions</button>
                <button onclick="openModal('privacyModal')" class="hover:text-brand-gold transition">Privacy Policy</button>
                <button onclick="openModal('returnsModal')" class="hover:text-brand-gold transition">Returns</button>
            </div>
            
            <div class="text-center text-[11px] text-brand-muted leading-relaxed max-w-3xl mx-auto space-y-4">
                <p>The statements on this website have not been evaluated by any regulatory authority. This product is not intended to diagnose, treat, cure or prevent any disease.</p>
                <p>The content and product offered on this website are based on the author's opinion and are provided on an "AS IS" and "AS AVAILABLE" basis. Always consult with a healthcare professional before starting any new diet, supplement, or exercise routine.</p>
                <div class="border border-white/10 rounded-lg p-4 bg-white/5 mt-4 text-[11px] font-semibold text-brand-textLight">
                    IMPORTANT NOTICE: We are an independent distributor (advertising partner) and NOT the manufacturer of this product. All sales are processed securely by the official manufacturer. We receive a commission for purchases made through the links on this website.
                </div>
            </div>

            <div class="border-t border-white/10 mt-8 pt-6 text-center text-xs text-brand-muted font-medium">
                &copy; 2026 Slimanol Official. All rights reserved.
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script>
        function toggleFaq(element) {
            const isActive = element.classList.contains('open');
            const allItems = document.querySelectorAll('.faq-item');
            allItems.forEach(item => {
                item.classList.remove('open');
            });
            if (!isActive) {
                element.classList.add('open');
            }
        }

        function openModal(id) {
            document.getElementById(id).classList.add('active');
        }

        function closeModal(id) {
            document.getElementById(id).classList.remove('active');
        }

        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', function(e) {
                if (e.target === this) {
                    this.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
"""

with open('c:\\Users\\Vinicius\\Desktop\\_Desktop_Organizado\\antigravity-skills\\antigravity-kit\\slimanol-offer\\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Slimanol index.html completely rewritten with Optivell/Sema7 layout!")
