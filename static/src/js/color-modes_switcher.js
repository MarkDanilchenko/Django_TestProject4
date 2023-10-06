try {
  const colorMode_switcher = localStorage.getItem("colorMode_switcher");
  if (colorMode_switcher === null) {
    throw new Error("The color theme switched to light-mode as default");
  } else {
    $("html").attr("data-bs-theme", `${colorMode_switcher}`);
  }
} catch (e) {
  $("html").attr("data-bs-theme", `${"light"}`);
  localStorage.setItem("colorMode_switcher", "light");
}

if (document.getElementById("colorMode_switcher")) {
  document.getElementById("colorMode_switcher").addEventListener("click", () => {
    const switcher = $("html").attr("data-bs-theme");
    if (switcher == "dark") {
      $("html").attr("data-bs-theme", "light");
      localStorage.setItem("colorMode_switcher", "light");
    } else if (switcher == "light") {
      $("html").attr("data-bs-theme", "dark");
      localStorage.setItem("colorMode_switcher", "dark");
    }
  });
}
