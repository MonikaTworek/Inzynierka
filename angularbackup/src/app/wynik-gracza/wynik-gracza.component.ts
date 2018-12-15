import { Component, OnInit } from '@angular/core';
import {ConnectToBlackJackService} from '../connect-to-black-jack.service';

@Component({
  selector: 'app-wynik-gracza',
  templateUrl: './wynik-gracza.component.html',
  styleUrls: ['./wynik-gracza.component.scss']
})
export class WynikGraczaComponent implements OnInit {
  Wynik: { [index: string]: any } = {};
  constructor(private server: ConnectToBlackJackService) { }

  ngOnInit() {
    this.Update(this.server.Set);
  }

  Update(tekst: any) {
    this.Wynik.Add('winning', tekst.player_score.winning);
    this.Wynik.Add('draw', tekst.player_score.draw);
    this.Wynik.Add('loosing', tekst.player_score.loosing);
    this.Wynik.Add('blackjack', tekst.player_score.blackjack);
    this.Wynik.Add('money', tekst.player_score.winning - tekst.player_score.loosing + 0.5 * tekst.player_score.blackjack);
  }

}
