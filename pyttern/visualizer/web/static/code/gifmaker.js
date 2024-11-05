const RATIO = 1/4;

async function generateGIF() {
    const pytternImages = [];
    const pythonImages = [];

    await start_simulator();
    for (let i = 0; i < max_step; i++) {
        await set_current_step(i);

        const pytternImage = pyttern_fsm_cy.png({ full: true, maxWidth: 1000, maxHeight: 1000});
        const pythonImage = python_tree_cy.png({ full: true, maxWidth: 1000, maxHeight: 1000 });

        pytternImages.push(pytternImage);
        pythonImages.push(pythonImage);
    }

    await createGif(pytternImages, pythonImages);
    pytternImages.length = 0;
    pythonImages.length = 0;
}

async function createGif(pytternImages, pythonImages) {
    const frames = [];

    // Load images and store their dimensions
    for (let i = 0; i < pytternImages.length; i++) {
        const pytternImage = new Image();
        const pythonImage = new Image();

        pytternImage.src = pytternImages[i];
        pythonImage.src = pythonImages[i];

        await Promise.all([
            new Promise(resolve => { pytternImage.onload = resolve; }),
            new Promise(resolve => { pythonImage.onload = resolve; })
        ]);

        // Log loaded images
        console.log(`Loaded images for frame ${i + 1}:`);
        console.log(`Pyttern Image - Width: ${pytternImage.width}, Height: ${pytternImage.height}`);
        console.log(`Python Image - Width: ${pythonImage.width}, Height: ${pythonImage.height}`);

        // Store frames and their sizes
        frames.push({ pytternImage, pythonImage });
    }

    // Calculate total width and max height for the GIF
    const totalWidth = frames.reduce((sum, frame) => Math.max(sum, frame.pytternImage.width + frame.pythonImage.width), 1);
    const maxHeight = Math.max(...frames.map(frame => Math.max(frame.pytternImage.height, frame.pythonImage.height)));

    console.log(`Total GIF width: ${totalWidth}, Max GIF height: ${maxHeight}`);

    // Create GIF with dynamic size
    let gif = new GIF({
        workers: 2,
        quality: 10,
        width: totalWidth,
        height: maxHeight,
        workerScript: 'static/code/gifs/gif.worker.js'
    });

    // Draw images onto canvas and add to GIF
    frames.forEach((frame, index) => {
        const canvas = document.createElement('canvas');
        canvas.width = totalWidth;
        canvas.height = maxHeight;
        const context = canvas.getContext('2d');
        context.fillStyle = 'white';
        context.fillRect(0, 0, canvas.width, canvas.height);

        // Draw each image pair
        let xOffset = 0;
        context.drawImage(frame.pytternImage, xOffset, 0, frame.pytternImage.width, frame.pytternImage.height);
        xOffset += frame.pytternImage.width;
        context.drawImage(frame.pythonImage, xOffset, 0, frame.pythonImage.width, frame.pythonImage.height);


        // Log the canvas size
        console.log(`Canvas size for frame ${index + 1}: Width: ${canvas.width}, Height: ${canvas.height}`);

        // Add the merged canvas to the GIF
        gif.addFrame(canvas, { delay: 500 });
        console.log(`Added frame ${index + 1} to GIF.`);
    });

    gif.on("start", function() {
        console.log('GIF creation started.');
    });

    gif.on("progress", function(progress) {
        console.log(`GIF creation progress: ${progress*100}%`);
    });

    // Finish the GIF creation process
    gif.on('finished', function(blob) {
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'generated.gif'; // Set the desired file name
        link.click(); // Simulate a click to download
        console.log('GIF created and downloaded successfully.');
        URL.revokeObjectURL(link.href); // Release the object URL
        frames.length = 0; // Clear the frames array
        for(worker of gif.freeWorkers){
            worker.terminate()
        }
        worker.frames.length = 0;
    });

    // Render the GIF
    let res = gif.render();
    if(!res) {
        console.error('Error rendering GIF.');
        return
    }
    console.log('Rendering GIF...');
}
