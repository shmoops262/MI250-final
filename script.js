const STARTING_POINTS = 10;

const scoreboardBody = document.getElementById("scoreboard-body");
const addMemberButton = document.getElementById("add-member");
const rowTemplate = document.getElementById("score-row-template");

const calculateTotal = (row) => {
  const inputs = row.querySelectorAll("input[data-points]");
  const adjustments = Array.from(inputs).reduce((total, input) => {
    const count = Number.parseInt(input.value, 10) || 0;
    const points = Number.parseInt(input.dataset.points, 10) || 0;
    return total + count * points;
  }, 0);

  const totalCell = row.querySelector(".total");
  totalCell.textContent = STARTING_POINTS + adjustments;
};

const registerRowEvents = (row) => {
  row.querySelectorAll("input").forEach((input) => {
    input.addEventListener("input", () => calculateTotal(row));
  });

  const removeButton = row.querySelector("[data-remove]");
  removeButton.addEventListener("click", () => row.remove());

  calculateTotal(row);
};

const addRow = (name = "") => {
  const clone = rowTemplate.content.firstElementChild.cloneNode(true);
  const nameInput = clone.querySelector(".field__input--name");
  nameInput.value = name;
  scoreboardBody.appendChild(clone);
  registerRowEvents(clone);
};

addMemberButton.addEventListener("click", () => addRow());

const defaultNames = [
  "Ava",
  "Nevaeh",
  "Brad",
  "Eli",
  "Alanna",
  "Bill",
  "Bo",
  "Braeden",
  "Brooke",
  "cam",
  "Cecelia",
  "Chad",
  "Charlie",
  "Erika",
  "grace",
  "Henry",
  "Hugh",
  "John",
  "Jon yb",
  "Kendall",
  "Kyra",
  "Liam",
  "mason",
  "Matt",
  "maya",
  "good Ryan",
  "bad Ryan",
  "Sabrina",
  "Sam",
  "Sam grace",
  "Sean",
  "sefina",
  "Sophia",
  "Taylor",
  "Sophia d",
  "Zander",
  "Tiago",
  "Tyler",
];

defaultNames.forEach((name) => addRow(name));
