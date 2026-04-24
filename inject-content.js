// inject-content.js

window.addEventListener("DOMContentLoaded", function() {

    // 1. Injecting Social Media Posts
    const socialMediaPostHTML = `
        <div class="post">
            <h2>Instagram Post</h2>
            <p>🌟 **Looking for high-quality print-on-demand products?**  
            Check out Printify! I’ve been using them for months, and they make creating custom merchandise super easy. Whether you're a designer or just want a unique product, they have everything you need! 🙌  
            👉 <a href="https://try.printify.com/r3xsnwqufe8t" class="cta-button" target="_blank">Get Started Here!</a>
            </p>
            <p>#PrintOnDemand #Printify #CustomMerch #MerchDesign #EntrepreneurLife #SideHustle</p>
        </div>
        <div class="post">
            <h2>Twitter Post</h2>
            <p>🚀 **Start your own custom merch line today with Printify!**  
            From t-shirts to accessories, Printify makes it easy to design, print, and sell products. No upfront costs.  
            Get started here: <a href="https://try.printify.com/r3xsnwqufe8t" class="cta-button" target="_blank">Sign Up Now!</a>
            </p>
            <p>#PrintOnDemand #SideHustle #MerchBusiness #Printify #Entrepreneur</p>
        </div>
    `;

    const socialPostContainer = document.createElement('div');
    socialPostContainer.innerHTML = socialMediaPostHTML;
    document.body.appendChild(socialPostContainer);  // Appends to the body of the page

    // 2. Injecting Email Capture Form
    const emailCaptureFormHTML = `
        <div class="email-capture-form">
            <h2>Get Your Free Guide: How to Start a Print-On-Demand Business</h2>
            <form id="email-form">
                <input type="email" id="email" placeholder="Enter your email" required style="padding: 10px; width: 80%; max-width: 300px;">
                <br><br>
                <button type="submit" class="cta-button">Get the Guide</button>
            </form>
        </div>
    `;
    const emailFormContainer = document.createElement('div');
    emailFormContainer.innerHTML = emailCaptureFormHTML;
    document.body.appendChild(emailFormContainer); // Appends to the body

    // 3. Injecting Exit-Intent Popup
    const exitIntentPopupHTML = `
        <div class="popup" id="exit-popup">
            <div class="popup-content">
                <h2>Wait! Don't Go Yet!</h2>
                <p>Sign up now and get 10% off your first Printify product. Start your shop today!</p>
                <a href="https://try.printify.com/r3xsnwqufe8t" class="cta-button">Claim Your Discount</a>
            </div>
        </div>
    `;
    const exitPopupContainer = document.createElement('div');
    exitPopupContainer.innerHTML = exitIntentPopupHTML;
    document.body.appendChild(exitPopupContainer);

    // 4. Injecting Social Proof Section
    const socialProofHTML = `
        <div class="post">
            <h2>Live Activity</h2>
            <p>💬 "John from New York just ordered a custom t-shirt!"</p>
            <p>💬 "Sarah from Texas just designed a new mug!"</p>
            <p>See how easy it is to create your own custom products with Printify.</p>
        </div>
    `;
    const socialProofContainer = document.createElement('div');
    socialProofContainer.innerHTML = socialProofHTML;
    document.body.appendChild(socialProofContainer);

    // 5. A/B Testing
    const abTestScript = `
        <script>
            const testGroup = Math.random() < 0.5 ? 'A' : 'B';
            if (testGroup === 'A') {
                document.querySelector('h1').textContent = 'Start Your Merch Store with Printify - Create Custom Products Easily';
            } else {
                document.querySelector('h1').textContent = 'Build Your Brand with Printify - Custom Products Made Easy';
            }

            // Exit Intent Popup Event
            document.addEventListener('mouseleave', function (e) {
                if (!e.toElement && !e.relatedTarget) { 
                    document.getElementById('exit-popup').style.display = 'flex';
                }
            });

            // Email Capture Form Submission
            document.getElementById('email-form').addEventListener('submit', function (e) {
                e.preventDefault();
                const email = document.getElementById('email').value;
                if (email) {
                    alert('Thank you for subscribing! Check your inbox for the guide.');
                    document.getElementById('email').value = '';  // Clear the input field
                }
            });
        </script>
    `;
    const scriptContainer = document.createElement('div');
    scriptContainer.innerHTML = abTestScript;
    document.body.appendChild(scriptContainer);

});
