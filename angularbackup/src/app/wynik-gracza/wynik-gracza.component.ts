import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-wynik-gracza',
  templateUrl: './wynik-gracza.component.html',
  styleUrls: ['./wynik-gracza.component.scss']
})
export class WynikGraczaComponent implements OnInit {
  Wynikwinning: any;
  Wynikdraw: any;
  Wynikloosing: any;
  Wynikblackjack: any;
  Wynikmoney: any;
  constructor(private server: ConnectToBlackJackService, private router: Router) { }

  ngOnInit() {
    this.Update(this.server.Set());
  }

  Update(tekst: any) {
    console.log(tekst);
    this.Wynikwinning = tekst.player_score.winning;
     // this.Wynikwinning = 0;
    this.Wynikdraw = tekst.player_score.draw;
    this.Wynikloosing = tekst.player_score.loosing;
    this.Wynikblackjack = tekst.player_score.winning;
    // this.Wynikdraw = 0;
    // this.Wynikloosing = 0;
    // this.Wynikblackjack = 0;
    this.Wynikmoney = (tekst.player_score.winning - tekst.player_score.loosing + 0.5 * tekst.player_score.blackjack) * 10;
    // this.Wynikmoney = 12;
  }

  ComeBack() {
    this.router.navigate(['/start']);
  }

}
