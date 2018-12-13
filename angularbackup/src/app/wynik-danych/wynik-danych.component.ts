import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-wynik-danych',
  templateUrl: './wynik-danych.component.html',
  styleUrls: ['./wynik-danych.component.scss']
})
export class WynikDanychComponent implements OnInit {
  Ekspansyjna: { [index: string]: number } = {};
  ReagujNaBank: { [index: string]: number } = {};
  HiLow: { [index: string]: number } = {};
  Intuicyjna: { [index: string]: number } = {};
  NeverBust: { [index: string]: number } = {};
  PrzelamPasse: { [index: string]: number } = {};
  PrzetrzymajPasse: { [index: string]: number } = {};
  Podstawowa: { [index: string]: number } = {};
  ZaleznaOdSzczescia: { [index: string]: number } = {};
  Pasujaca: { [index: string]: number } = {};
  Idealna: { [index: string]: number } = {};  constructor() { }

  ngOnInit() {
  }

  Update(tekst) {
    this.Ekspansyjna.Add('winning', tekst.bots_score.Ekspansyjna.winning);
    this.Ekspansyjna.Add('draw', tekst.bots_score.Ekspansyjna.draw);
    this.Ekspansyjna.Add('loosing', tekst.bots_score.Ekspansyjna.loosing);
    this.Ekspansyjna.Add('blackjack', tekst.bots_score.Ekspansyjna.blackjack);
    this.Ekspansyjna.Add('money', tekst.bots_score.Ekspansyjna.winning - tekst.bots_score.Ekspansyjna.loosing + 0.5 * tekst.bots_score.Ekspansyjna.blackjack);
  }
}

// {
//   "bots_score": [
//   {
//     "Ekspansyjna": {
//       "blackjack": 1,
//       "draw": 1,
//       "loosing": 2,
//       "winning": 5
//     }
//   },
//   {
//     "ReagujNaBank": {
//       "blackjack": 0,
//       "draw": 1,
//       "loosing": 5,
//       "winning": 2
//     }
//   },
//   {
//     "HILow": {
//       "blackjack": 0,
//       "draw": 0,
//       "loosing": 5,
//       "winning": 4
//     }
//   },
//   {
//     "Intuicyjna": {
//       "blackjack": 0,
//       "draw": 0,
//       "loosing": 6,
//       "winning": 3
//     }
//   },
//   {
//     "NeverBust": {
//       "blackjack": 0,
//       "draw": 0,
//       "loosing": 5,
//       "winning": 5
//     }
//   },
//   {
//     "NeverBust": {
//       "blackjack": 0,
//       "draw": 0,
//       "loosing": 6,
//       "winning": 3
//     }
//   },
//   {
//     "PrzelamPasse": {
//       "blackjack": 0,
//       "draw": 1,
//       "loosing": 7,
//       "winning": 1
//     }
//   },
//   {
//     "PrzetrzymajPasse": {
//       "blackjack": 0,
//       "draw": 1,
//       "loosing": 5,
//       "winning": 3
//     }
//   },
//   {
//     "Podstawowa": {
//       "blackjack": 0,
//       "draw": 1,
//       "loosing": 6,
//       "winning": 2
//     }
//   },
//   {
//     "ZaleznaOdSzczescia": {
//       "blackjack": 0,
//       "draw": 1,
//       "loosing": 6,
//       "winning": 3
//     }
//   },
//   {
//     "Pasujaca": {
//       "blackjack": 1,
//       "draw": 0,
//       "loosing": 4,
//       "winning": 6
//     }
//   },
//   {
//     "Idealna": {
//       "blackjack": 1,
//       "draw": 1,
//       "loosing": 1,
//       "winning": 6
//     }
//   }
// ],
//   "header": "success",
//   "player_score": {
//   "blackjack": 0,
//     "draw": 0,
//     "loosing": 0,
//     "winning": 0
// }
// }
