import { Component, OnInit } from '@angular/core';
import {Card} from '../Card.model';
import {TableService} from '../table.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-widok',
  templateUrl: './widok.component.html',
  styleUrls: ['./widok.component.scss']
})
export class WidokComponent implements OnInit {
  Row1: Card[];
  Row2: Card[];
  Row3: Card[];

  map = new Map([
    [ 'Karo1', 'assets/card/Karo1.jpg' ],
    [ 'Karo2', 'assets/card/Karo2.jpg' ],
    [ 'Karo3', 'assets/card/Karo3.jpg' ],
    [ 'Karo4', 'assets/card/Karo4.jpg' ],
    [ 'Karo5', 'assets/card/Karo5.jpg' ],
    [ 'Karo6', 'assets/card/Karo6.jpg' ],
    [ 'Karo7', 'assets/card/Karo7.jpg' ],
    [ 'Karo8', 'assets/card/Karo8.jpg' ],
    [ 'Karo9', 'assets/card/Karo9.jpg' ],
    [ 'Karo10', 'assets/card/Karo10.jpg' ],
    [ 'Karo11', 'assets/card/Karo11.jpg' ],
    [ 'Karo12', 'assets/card/Karo12.jpg' ],
    [ 'Karo13', 'assets/card/Karo13.jpg' ],
    [ 'Kier1', 'assets/card/Kier1.jpg' ],
    [ 'Kier2', 'assets/card/Kier2.jpg' ],
    [ 'Kier3', 'assets/card/Kier3.jpg' ],
    [ 'Kier4', 'assets/card/Kier4.jpg' ],
    [ 'Kier5', 'assets/card/Kier5.jpg' ],
    [ 'Kier6', 'assets/card/Kier6.jpg' ],
    [ 'Kier7', 'assets/card/Kier7.jpg' ],
    [ 'Kier8', 'assets/card/Kier8.jpg' ],
    [ 'Kier9', 'assets/card/Kier9.jpg' ],
    [ 'Kier10', 'assets/card/Kier10.jpg' ],
    [ 'Kier11', 'assets/card/Kier11.jpg' ],
    [ 'Kier12', 'assets/card/Kier12.jpg' ],
    [ 'Kier13', 'assets/card/Kier13.jpg' ],
    [ 'Trefl1', 'assets/card/Trefl1.jpg' ],
    [ 'Trefl2', 'assets/card/Trefl2.jpg' ],
    [ 'Trefl3', 'assets/card/Trefl3.jpg' ],
    [ 'Trefl4', 'assets/card/Trefl4.jpg' ],
    [ 'Trefl5', 'assets/card/Trefl5.jpg' ],
    [ 'Trefl6', 'assets/card/Trefl6.jpg' ],
    [ 'Trefl7', 'assets/card/Trefl7.jpg' ],
    [ 'Trefl8', 'assets/card/Trefl8.jpg' ],
    [ 'Trefl9', 'assets/card/Trefl9.jpg' ],
    [ 'Trefl10', 'assets/card/Trefl10.jpg' ],
    [ 'Trefl11', 'assets/card/Trefl11.jpg' ],
    [ 'Trefl12', 'assets/card/Trefl12.jpg' ],
    [ 'Trefl13', 'assets/card/Trefl13.jpg' ],
    [ 'Pik1', 'assets/card/Pik1.jpg' ],
    [ 'Pik2', 'assets/card/Pik2.jpg' ],
    [ 'Pik3', 'assets/card/Pik3.jpg' ],
    [ 'Pik4', 'assets/card/Pik4.jpg' ],
    [ 'Pik5', 'assets/card/Pik5.jpg' ],
    [ 'Pik6', 'assets/card/Pik6.jpg' ],
    [ 'Pik7', 'assets/card/Pik7.jpg' ],
    [ 'Pik8', 'assets/card/Pik8.jpg' ],
    [ 'Pik9', 'assets/card/Pik9.jpg' ],
    [ 'Pik10', 'assets/card/Pik10.jpg' ],
    [ 'Pik11', 'assets/card/Pik11.jpg' ],
    ['Pik12', 'assets/card/Pik12.jpg' ],
    [ 'Pik13', 'assets/card/Pik13.jpg' ],
    ['face_down', 'assets/card/face_down.jpg']
  ]);

  constructor(private table: TableService) { }

  ngOnInit() {
    this.table.GetRow1().subscribe(x => this.Row1 = x );
    this.table.GetRow2().subscribe( y => this.Row2 = y);
    this.table.GetRow3().subscribe(z => this.Row3 = z);
  }

  getCardUrl(card: Card) {
    if (card.color === 'face_down') {
      return this.map.get('face_down');
    }
    /*console.log(card, card.color + card.rank, this.map.get(card.color + card.rank));*/
    return this.map.get(card.color + card.rank);
  }


}


