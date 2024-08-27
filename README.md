<h1 align="center">🎯 Weighted Token Sampler 🎯</h1>


<h5 align="center">Project Page: https://shure-dev.github.io/weighted-token-sampler/</h5>

<p align="center">
  <!-- <img src="https://img.freepik.com/premium-vector/abstract-circle-circular-wave-wavy-lines-futuristic-bright-futurism-minimalist-vector-logo-design_216988-1808.jpg" alt="Logo" style="width:200px; height:auto;"> -->
  <img src="diagram/image.png" alt="Logo" style="width:600px; height:auto;">
<!-- ![alt text](/images/image.png) -->

</p>


<p align="center">
  <em>Boost prediction accuracy using weighted token sampling</em>
  
</p>

<hr>

<h2>🔍 Overview</h2>

<p>
  <strong>Weighted Token Sampler</strong> is a simple tool that improves prediction accuracy by calculating the weighted average of token probabilities. It's designed for tasks where precise predictions are needed within a defined range.
</p>

<h2>💻 Installation</h2>

<p>Install the package with:</p>

<pre><code>pip install git+https://github.com/your_username/weighted_token_sampler.git</code></pre>

<h2>🚀 Quick Start</h2>

<p>Here’s how to use the package:</p>

<pre><code>from weighted_token_sampler.main_module import ImageProcessor

# Initialize with your API key
processor = ImageProcessor(api_key="your_api_key_here")

# Generate points and get predictions
points = processor.generate_evenly_spaced_points(10)
for i, point in enumerate(points):
    response_x, response_y, _ = processor.process_image_and_get_response(point, i)
    print(f"Point: {point}, X: {response_x}, Y: {response_y}")
</code></pre>

<h2>🏁 Conclusion</h2>

<p>
  <strong>Weighted Token Sampler</strong> is a straightforward tool to enhance prediction accuracy. Try it out in your projects to see the benefits!
</p>