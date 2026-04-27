export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,513',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, it is estimated that ${budget.income} were reported, ${budget.gdp} budget, with a per capita of ${budget.capita}.`;
}
