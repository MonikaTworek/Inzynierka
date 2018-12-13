import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-wynik-gracza',
  templateUrl: './wynik-gracza.component.html',
  styleUrls: ['./wynik-gracza.component.scss']
})
export class WynikGraczaComponent implements OnInit {
  Wynik: { [index: string]: number } = {};
  constructor() { }

  ngOnInit() {
  }

  Update(tekst) {
    this.Wynik.Add('winning', tekst.player_score.winning);
    this.Wynik.Add('draw', tekst.player_score.draw);
    this.Wynik.Add('loosing', tekst.player_score.loosing);
    this.Wynik.Add('blackjack', tekst.player_score.blackjack)
    this.Wynik.Add('money', tekst.player_score.winning - tekst.player_score.loosing + 0.5 * tekst.player_score.blackjack);
  }

}


// {
//   "bots_score": [
//   {
//     "name": "Ekspansyjna",
//     "score": {
//       "draw": 0,
//       "loosing": 7,
//       "winning": 1
//     }
//   },
//   {
//     "name": "ReagujNaBank",
//     "score": {
//       "draw": 2,
//       "loosing": 4,
//       "winning": 3
//     }
//   },
//   {
//     "name": "HILow",
//     "score": {
//       "draw": 0,
//       "loosing": 6,
//       "winning": 4
//     }
//   },
//   {
//     "name": "Intuicyjna",
//     "score": {
//       "draw": 0,
//       "loosing": 8,
//       "winning": 2
//     }
//   },
//   {
//     "name": "NeverBust",
//     "score": {
//       "draw": 1,
//       "loosing": 3,
//       "winning": 6
//     }
//   },
//   {
//     "name": "NeverBust",
//     "score": {
//       "draw": 0,
//       "loosing": 5,
//       "winning": 5
//     }
//   },
//   {
//     "name": "PrzelamPasse",
//     "score": {
//       "draw": 1,
//       "loosing": 8,
//       "winning": 1
//     }
//   },
//   {
//     "name": "PrzetrzymajPasse",
//     "score": {
//       "draw": 0,
//       "loosing": 5,
//       "winning": 4
//     }
//   },
//   {
//     "name": "Podstawowa",
//     "score": {
//       "draw": 0,
//       "loosing": 6,
//       "winning": 4
//     }
//   },
//   {
//     "name": "ZaleznaOdSzczescia",
//     "score": {
//       "draw": 0,
//       "loosing": 6,
//       "winning": 4
//     }
//   },
//   {
//     "name": "Pasujaca",
//     "score": {
//       "draw": 1,
//       "loosing": 2,
//       "winning": 7
//     }
//   },
//   {
//     "name": "Idealna",
//     "score": {
//       "draw": 1,
//       "loosing": 2,
//       "winning": 7
//     }
//   }
// ],
//   "header": "success",
//   "player_score": {
//   "draw": 0,
//     "loosing": 0,
//     "winning": 0
// }
// }
