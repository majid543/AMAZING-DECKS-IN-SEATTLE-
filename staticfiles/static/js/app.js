

 $(document).ready(function () {
    console.log("Document Ready");
    $('.project').click(function () {
        var projectId = $(this).data('project-id'); // Get the project ID from the data attribute
        console.log("Image Clicked for Project ID:", projectId);

        // Send an AJAX request to fetch project photos
        var url = '/fetch_project_photos/' + projectId + '/';

        // Send an AJAX request to fetch project photos using the fetch API
        fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                // Add any other headers if needed
            },
        })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(function (data) {
            // Process the data and display the photos in a modal
            displayPhotos(data.photos); // You will need to implement this function
        })
        .catch(function (error) {
            console.error("Error fetching project photos:", error);
        });
    });

    // Placeholder for the displayPhotos function
    function displayPhotos(photos) {
        // Clear any previous images
        $('#image-gallery').empty();

        // Append the new images to the gallery
        for (var i = 0; i < photos.length; i++) {
            var imageUrl = photos[i].url;
            var imgElement = $('<img>').attr('src', imageUrl);
            $('#image-gallery').append(imgElement);
        }

        // Show the image gallery
        $('#image-gallery').show();
    }
});



$(document.body).click(function (event) {
    if (!$(event.target).closest('#image-gallery').length) {
        $('#image-gallery').hide();
    }
});



var images = document.querySelectorAll('.slideshow-image');
        var currentIndex = 0;

        function showImage(index) {
            // Hide all images
            images.forEach(function (image) {
                image.style.opacity = 0;
            });

            // Show the selected image
            images[index].style.opacity = 1;
        }

        function nextImage() {
            currentIndex = (currentIndex + 1) % images.length;
            showImage(currentIndex);
        }

        // Initially, show the first image
        showImage(currentIndex);

        // Change image every 1 second
        setInterval(nextImage, 1000);


function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to add the .animate class when the element is in the viewport
function handleScroll() {
    const elementsToAnimate = document.querySelectorAll('.scroll-animation');
    elementsToAnimate.forEach((el) => {
        if (isElementInViewport(el) && !el.classList.contains('animate')) {
            el.classList.add('animate');
        }
    });
}

// Attach a scroll event listener to trigger the animation
window.addEventListener('scroll', handleScroll);



let currentQuestion = 0;
    
    function nextQuestion() {
        const questionSections = document.querySelectorAll('.questionSection');
        questionSections[currentQuestion].classList.add('hidden');
        currentQuestion++;
        if (currentQuestion < questionSections.length) {
            questionSections[currentQuestion].classList.remove('hidden');
        }
    }

    function calculateCharges() {
        // Perform calculations and get service charges
        // You may need to use AJAX to send data to the server and receive the result
        const serviceCharges = calculate_service_charges(/* pass data here */);

        // Display the result
        document.getElementById('serviceCharges').textContent = serviceCharges;

        // Show the result section
        document.querySelector('.resultSection').classList.remove('hidden');
    }