function toggleFunction() {
   
    var x = document.getElementById("topnav");
    x.classList.toggle("expanded");
}

function checkOrientation() {
    var x = document.getElementById("topnav");
    if (window.matchMedia("(orientation: landscape)").matches) { // Change the class name to "landscape" when in landscape orientation

        if (x.className === "nav-container responsive") {
            x.className = "nav-container"
        }


    } else {}
}


//scroll animations 
const scrollElements = document.querySelectorAll(".js-scroll");

const elementInView = (el, dividend = 1) => {
  const elementTop = el.getBoundingClientRect().top;

  return (
    elementTop <=
    (window.innerHeight || document.documentElement.clientHeight) / dividend
  );
};

const elementOutofView = (el) => {
  const elementTop = el.getBoundingClientRect().top;

  return (
    elementTop > (window.innerHeight || document.documentElement.clientHeight)
  );
};

const displayScrollElement = (element) => {
  element.classList.add("scrolled");
};

const hideScrollElement = (element) => {
  element.classList.remove("scrolled");
};

const handleScrollAnimation = () => {
  scrollElements.forEach((el) => {
    if (elementInView(el, 1.25)) {
      displayScrollElement(el);
    } else if (elementOutofView(el)) {
      hideScrollElement(el)
    }
  })
}

window.addEventListener("scroll", () => { 
  handleScrollAnimation();
});


const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.tabTarget)
    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active')
    })
    tabs.forEach(tab => {
      tab.classList.remove('active')
    })
    tab.classList.add('active')
    target.classList.add('active')
  })
})

var slider1 = document.getElementById('slider1'),
sliderItems = document.getElementById('slides'),
prev = document.getElementById('prev'),
next = document.getElementById('next');
// pagination = document.getElementById('pagination');

function slide(wrapper, items, prev, next) {
var posX1 = 0,
    posX2 = 0,
    posInitial,
    posFinal,
    threshold = 100,
    slides = items.getElementsByClassName('slide'),
    slidesLength = slides.length,
    slideSize = items.getElementsByClassName('slide')[0].offsetWidth,
    firstSlide = slides[0],
    lastSlide = slides[slidesLength - 1],
    cloneFirst = firstSlide.cloneNode(true),
    cloneLast = lastSlide.cloneNode(true),
    index = 0,
    allowShift = true;

// Clone first and last slide
items.appendChild(cloneFirst);
items.insertBefore(cloneLast, firstSlide);
wrapper.classList.add('loaded');

// Mouse events
items.onmousedown = dragStart;

// Touch events
items.addEventListener('touchstart', dragStart);
items.addEventListener('touchend', dragEnd);
items.addEventListener('touchmove', dragAction);

// Click events
prev.addEventListener('click', function () {
    shiftSlide(-1)
});
next.addEventListener('click', function () {
    shiftSlide(1)
});

// Transition events
items.addEventListener('transitionend', checkIndex);

var autoplayInterval = setInterval(function () {
    shiftSlide(1);
}, 5000);
// Change the interval as needed

// Pause autoplay on hover
wrapper.addEventListener('mouseenter', function () {
    clearInterval(autoplayInterval);
});

// Resume autoplay on mouse leave
wrapper.addEventListener('mouseleave', function () {
    autoplayInterval = setInterval(function () {
        shiftSlide(1);
    }, 5000); // Change the interval as needed
});


function dragStart(e) {
    e = e || window.event;
    // e.preventDefault();
    e.stopPropagation();
    posInitial = items.offsetLeft;

    if (e.type == 'touchstart') {
        posX1 = e.touches[0].clientX;
    } else {
        posX1 = e.clientX;
        document.onmouseup = dragEnd;
        document.onmousemove = dragAction;
    }
}

function dragAction(e) {
    e = e || window.event;

    if (e.type == 'touchmove') {
        posX2 = posX1 - e.touches[0].clientX;
        posX1 = e.touches[0].clientX;
    } else {
        posX2 = posX1 - e.clientX;
        posX1 = e.clientX;
    } items.style.left = (items.offsetLeft - posX2) + "px";
}



function dragEnd(e) {
    posFinal = items.offsetLeft;
    if (posFinal - posInitial < - threshold) {
        shiftSlide(1, 'drag');
    } else if (posFinal - posInitial > threshold) {
        shiftSlide(-1, 'drag');
    } else {
        items.style.left = (posInitial) + "px";
    }

    document.onmouseup = null;
    document.onmousemove = null;
}

function shiftSlide(dir, action) {
    items.classList.add('shifting');

    if (allowShift) {
        if (!action) {
            posInitial = items.offsetLeft;
        }

        if (dir == 1) {
            items.style.left = (posInitial - slideSize) + "px";
            index++;
        } else if (dir == -1) {
            items.style.left = (posInitial + slideSize) + "px";
            index--;
        }
    };

    allowShift = false;
}

function checkIndex() {
    items.classList.remove('shifting');

    if (index == -1) {
        items.style.left = -(slidesLength * slideSize) + "px";
        index = slidesLength - 1;
    }

    if (index == slidesLength) {
        items.style.left = -(1 * slideSize) + "px";
        index = 0;
    }

    allowShift = true;
}

}

slide(slider1, sliderItems, prev, next);

// lighthouse
// script.js

function openLightbox(src) {
  document.getElementById('lightbox').style.display = 'block';
  document.getElementById('lightbox-img').src = src;
}

function closeLightbox() {
  document.getElementById('lightbox').style.display = 'none';
}

// Close the lightbox when clicking anywhere outside of the image
document.getElementById('lightbox').addEventListener('click', function(event) {
  if (event.target === document.getElementById('lightbox')) {
      closeLightbox();
  }
});


